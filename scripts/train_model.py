import cupy as cp
import joblib
import pandas as pd
import os
import numpy as np
from scipy.sparse import issparse
from tqdm import tqdm

def inspect_matrix(matrix):
    print(f"Matrix type: {type(matrix)}")
    print(f"Matrix shape: {matrix.shape}")
    print(f"Matrix dtype: {matrix.dtype}")
    if issparse(matrix):
        print("Matrix is sparse")
        print(f"Non-zero elements: {matrix.nnz}")
        print(f"Density: {matrix.nnz / (matrix.shape[0] * matrix.shape[1]):.4f}")
    else:
        print("Matrix is dense")
    print(f"Sample of matrix:\n{matrix[:5, :5]}")
    print(f"Any NaN values: {np.isnan(matrix.data if issparse(matrix) else matrix).any()}")
    print(f"Any infinite values: {np.isinf(matrix.data if issparse(matrix) else matrix).any()}")

def compute_cosine_similarity_batched(matrix_gpu, output_dir, batch_size=1000):
    n = matrix_gpu.shape[0]
    matrix_norm = cp.linalg.norm(matrix_gpu, axis=1)

    for i in tqdm(range(0, n, batch_size)):
        end_i = min(i + batch_size, n)
        batch_i = matrix_gpu[i:end_i]

        for j in range(0, n, batch_size):
            end_j = min(j + batch_size, n)
            batch_j = matrix_gpu[j:end_j]

            # Compute dot product between batches
            dot_product = cp.dot(batch_i, batch_j.T)

            # Compute cosine similarity for the batches
            norm_i = matrix_norm[i:end_i]
            norm_j = matrix_norm[j:end_j]
            similarity_batch = dot_product / cp.outer(norm_i, norm_j)

            # Move the batch to CPU and save it
            output_file = os.path.join(output_dir, f"cosine_sim_{i}_{j}.npy")
            np.save(output_file, cp.asnumpy(similarity_batch))

        # Clear GPU memory
        cp.get_default_memory_pool().free_all_blocks()

def main():
    base_dir = os.path.dirname(__file__)
    preprocessed_data_path = os.path.join(base_dir, '..', 'data', 'processed_data')
    model_path = os.path.join(base_dir, '..', 'model')

    try:
        tfidf_matrix_path = os.path.join(preprocessed_data_path, "tfidf_matrix.pkl")
        postings_csv_path = os.path.join(preprocessed_data_path, "processed_postings.csv")

        print(f"Loading TF-IDF matrix from: {tfidf_matrix_path}")
        tfidf_matrix = joblib.load(tfidf_matrix_path)
        print("Inspecting loaded TF-IDF matrix:")
        inspect_matrix(tfidf_matrix)

        print(f"\nLoading postings data from: {postings_csv_path}")
        postings_df = pd.read_csv(postings_csv_path)
        print(f"Postings data loaded successfully. Shape: {postings_df.shape}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    try:
        print(f"\nConverting TF-IDF matrix to dense array if sparse...")
        if issparse(tfidf_matrix):
            tfidf_matrix = tfidf_matrix.toarray()

        print(f"Converting TF-IDF matrix to float32...")
        tfidf_matrix = tfidf_matrix.astype(np.float32)
        print("Inspecting converted TF-IDF matrix:")
        inspect_matrix(tfidf_matrix)

        print(f"\nConverting TF-IDF matrix to CuPy array...")
        tfidf_matrix_gpu = cp.array(tfidf_matrix)
        print(f"TF-IDF matrix conversion to GPU successful. Shape: {tfidf_matrix_gpu.shape}")

        print(f"Computing cosine similarity on GPU (batched)...")
        output_dir = os.path.join(model_path, "cosine_similarity")
        os.makedirs(output_dir, exist_ok=True)
        compute_cosine_similarity_batched(tfidf_matrix_gpu, output_dir)
        print(f"Cosine similarity computed successfully and saved to: {output_dir}")
    except Exception as e:
        print(f"Error during computation: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    main()