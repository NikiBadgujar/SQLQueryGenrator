def build_prompt(question):

    schema = """
customers(
    id,
    customer_name,
    city
)

orders(
    id,
    customer_id,
    amount,
    order_date
)
"""

    return f"""
### Database Schema

{schema}

### Task

Generate a SQL query for the following question.

Return ONLY SQL.

Question:
{question}
"""