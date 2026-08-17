import duckdb


def main() -> None:

    result = duckdb.sql("""
        SELECT
            country,
            COUNT(*) AS sales_count,
            SUM(revenue) AS total_revenue,
            AVG(revenue) AS average_revenue
        FROM 'sales.csv'
        GROUP BY country
        ORDER BY total_revenue DESC
        """)

    print(result)

    # Convert the result to a Pandas DataFrame if you need it.
    df = result.df()
    print(df)

    # Or even simpler
    duckdb.sql("""
        SELECT *
        FROM 'sales.csv'
        WHERE revenue > 500
    """).show()


if __name__ == "__main__":
    main()
