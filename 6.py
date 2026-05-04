# 6. Implement any one of the following Expert System
# 		I. Information management

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}
        
    def add_rule(self, condition, conclusion):
        self.rules.append({"condition": condition, "conclusion": conclusion})
    
    def add_fact(self, key, value):
        self.facts[key] = value
    
    def evaluate_condition(self, condition):
        for key, expected in condition.items():
            if key not in self.facts or self.facts[key] != expected:
                return False
        return True
    
    def infer(self):
        conclusions = []
        for rule in self.rules:
            if self.evaluate_condition(rule["condition"]):
                conclusions.append(rule["conclusion"])
        return conclusions

def information_management_system():
    print("=" * 60)
    print("EXPERT SYSTEM FOR INFORMATION MANAGEMENT")
    print("=" * 60)
    print("\nSelect Domain:")
    print("1. Database Selection")
    print("2. Data Security Level")
    print("3. Storage Decision")
    print("4. Information Retrieval Method")
    
    choice = input("\nEnter choice (1-4): ")
    es = ExpertSystem()
    
    if choice == "1":
        print("\n--- DATABASE SELECTION EXPERT ---")
        data_size = input("Data Size (small/medium/large): ").lower()
        concurrent = input("Concurrent Users (low/high): ").lower()
        structure = input("Data Structure (structured/semi-structured/unstructured): ").lower()
        
        es.add_fact("data_size", data_size)
        es.add_fact("concurrent", concurrent)
        es.add_fact("structure", structure)
        
        es.add_rule({"data_size": "small", "structure": "structured"}, "Use SQLite or MySQL")
        es.add_rule({"data_size": "medium", "structure": "structured"}, "Use PostgreSQL or MySQL")
        es.add_rule({"data_size": "large", "structure": "structured"}, "Use Oracle or PostgreSQL")
        es.add_rule({"structure": "unstructured"}, "Use MongoDB or NoSQL Database")
        es.add_rule({"structure": "semi-structured"}, "Use JSON-based DB or MongoDB")
        es.add_rule({"concurrent": "high"}, "Add: Use Database Clustering")
        
    elif choice == "2":
        print("\n--- DATA SECURITY EXPERT ---")
        data_type = input("Data Type (public/internal/confidential): ").lower()
        users = input("Number of Users (few/many): ").lower()
        
        es.add_fact("data_type", data_type)
        es.add_fact("users", users)
        
        es.add_rule({"data_type": "public"}, "Security Level: Low - Basic encryption")
        es.add_rule({"data_type": "internal"}, "Security Level: Medium - Authentication + Encryption")
        es.add_rule({"data_type": "confidential"}, "Security Level: High - Full encryption, Access controls, Audit logs")
        es.add_rule({"users": "many"}, "Add: Role-based Access Control (RBAC)")
        
    elif choice == "3":
        print("\n--- STORAGE DECISION EXPERT ---")
        access_freq = input("Access Frequency (high/low): ").lower()
        retention = input("Data Retention (short/long): ").lower()
        
        es.add_fact("access_freq", access_freq)
        es.add_fact("retention", retention)
        
        es.add_rule({"access_freq": "high", "retention": "short"}, "Use SSD Storage - Fast access")
        es.add_rule({"access_freq": "low", "retention": "short"}, "Use HDD Storage - Cost effective")
        es.add_rule({"retention": "long"}, "Use Cloud Storage with backup")
        es.add_rule({"access_freq": "high"}, "Consider Caching layer")
        
    elif choice == "4":
        print("\n--- INFORMATION RETRIEVAL EXPERT ---")
        search_type = input("Search Type (exact/partial/analytical): ").lower()
        volume = input("Data Volume (small/medium/large): ").lower()
        
        es.add_fact("search_type", search_type)
        es.add_fact("volume", volume)
        
        es.add_rule({"search_type": "exact", "volume": "small"}, "Use Simple SQL Queries")
        es.add_rule({"search_type": "exact", "volume": "large"}, "Use Indexed Search (Elasticsearch)")
        es.add_rule({"search_type": "partial"}, "Use Full-text Search")
        es.add_rule({"search_type": "analytical"}, "Use Data Warehouse with OLAP")
        es.add_rule({"volume": "large"}, "Add: Implement pagination and caching")
        
    results = es.infer()
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS:")
    print("=" * 60)
    for r in results:
        print(f"  - {r}")
    
    if not results:
        print("  No recommendations found for given criteria.")

if __name__ == "__main__":
    while True:
        information_management_system()
        cont = input("\nContinue? (yes/no): ").lower()
        if cont != "yes":
            print("Goodbye!")
            break