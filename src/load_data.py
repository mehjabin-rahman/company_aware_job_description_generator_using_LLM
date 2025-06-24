#pip install datasets
from datasets import load_dataset

def load_linkedin_job_postings(dataset_name="xanderios/linkedin-job-postings"):
    """
    Loads the LinkedIn job postings dataset from Hugging Face.

    Parameters:
        dataset_name (str): The dataset identifier on Hugging Face.

    Returns:
        DatasetDict: The loaded dataset.
    """
    try:
        ds = load_dataset(dataset_name)
        return ds
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
def analyze_data(dataset):
    data=dataset["train"]
    #print(data[0])
    print(data.features)
def main():
    dataset = load_linkedin_job_postings()
    if dataset:
        #print(dataset)
        analyze_data(dataset)

if __name__ == "__main__":
    main()
