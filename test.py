import time
from agent import ask_bank

def run_test(question):
    print(f"\n{'='*60}")
    print(f"Question: {question}")
    cols, rows, sql = ask_bank(question)
    if cols:
        print(f"SQL Generated: {sql}")
        print(f"Columns: {cols}")
        print(f"Results: {rows[:3]}")
        print(f"Status: PASSED ✅")
    else:
        print(f"Error: {sql}")
        print(f"Status: FAILED ❌")
    
    time.sleep(15)  # Wait 15 seconds between each request

if __name__ == "__main__":
    print("Running BankQuery AI Tests...")
    print("="*60)

    run_test("How many customers do we have?")
    run_test("What is the average transaction amount?")
    run_test("Show top 5 customers by total spending")
    run_test("How many male vs female customers do we have?")
    run_test("What is the most popular payment type?")
    run_test("Show customers with credit score above 750")
    run_test("Which location has the highest spending?")

    print(f"\n{'='*60}")
    print("All tests completed!")