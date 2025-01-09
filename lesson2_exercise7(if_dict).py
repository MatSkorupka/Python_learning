company_data = {
    "departments": {
        "IT": {
            "teams": {
                "development": {
                    "employees": ["John", "Alice", "Bob"],
                    "projects": {
                        "website": {"budget": 50000, "deadline": "2024-06"},
                        "mobile_app": {"budget": 100000, "deadline": "2024-12"}
                    },
                    "resources": {"laptops": 5, "monitors": 10}
                },
                "support": {
                    "employees": ["Carol", "Dave"],
                    "projects": {
                        "helpdesk": {"budget": 30000, "deadline": "2024-12"}
                    },
                    "resources": {"laptops": 2, "phones": 2}
                }
            },
            "budget_total": 200000
        }
    }
}

# Exercise 1: Access
# Get total number of employees in development team
# Get budget for mobile_app project
# Get total number of laptops in IT department (both teams)

print(f'Number of employees in development team {len(company_data['departments']['IT']['teams']['development']['employees'])}')
print(f'Budget for mobile_app project {company_data['departments']['IT']['teams']['development']['projects']['mobile_app']['budget']}')
print(f'Total number of laptops in IT department {company_data['departments']['IT']['teams']['development']['resources']['laptops'] + company_data['departments']['IT']['teams']['support']['resources']['laptops']}')



# Exercise 2: Data extraction
# Get list of all projects and their budgets
# Get all resources across all teams
# Get list of all projects and their budgets

# Store team references
dev_team = company_data['departments']['IT']['teams']['development']
support_team = company_data['departments']['IT']['teams']['support']

# Get project budgets
website_budget = dev_team['projects']['website']['budget']
mobile_budget = dev_team['projects']['mobile_app']['budget']
helpdesk_budget = support_team['projects']['helpdesk']['budget']

projects_and_budgets = {
    'website': website_budget,
    'mobile_app': mobile_budget,
    'helpdesk': helpdesk_budget
}
print("Projects and budgets:", projects_and_budgets)

# Get resources
dev_resources = dev_team['resources']
support_resources = support_team['resources']

all_resources = {
    'development': dev_resources,
    'support': support_resources
}
print("All resources:", all_resources)

