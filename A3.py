from parse import process_query
import ranking
from search import Searcher
import time

# "C:\\Users\\fight\\OneDrive\\Desktop\\CS121\\Assignment3\\CS121_SearchEngine\\DEV"
def main() -> None:
    """
    Run the program
    """
    with Searcher("resources\\final.jsonl", "resources\\doc_id_map.csv") as searcher:
        q = input("Enter your query!: ")
        while (q != "quit"):
            query = process_query(q)
            start_time = time.time()
            results = searcher.conjunctive_search_set(query)
            if results:
                ranked_results = ranking.merge_scores(results, query)
                print("Ranked Documents")
                for url, score in ranked_results:
                    print(searcher.get_url_from_csv(url)[0])
                end_time = time.time()  # Record the end time
                elapsed_time = end_time - start_time  # Compute duration
                print(f"FINAL Execution time: {elapsed_time:.6f} seconds")
            q = input("Enter your query!: ")

if __name__ == "__main__":
    main()
