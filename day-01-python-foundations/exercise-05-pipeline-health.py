"""
Exercise: Pipeline Health Status
Student: Samikshya Giri
Day: 1
"""


def check_pipeline_health(rows_loaded, rows_failed, runtime_minutes):
    """Calculate failure rate and classify pipeline status."""
    failure_rate = (rows_failed / rows_loaded) * 100

    # Healthy requires BOTH a low failure rate AND an acceptable runtime.
    # A low failure rate with a long runtime is NOT healthy, it is a
    # warning, because slow runtime is itself a health risk even when
    # the data is failing at an acceptable rate.
    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"

    # Catch the edge case: low failure rate but runtime too high
    if failure_rate <= 2 and runtime_minutes > 20:
        status = "Warning"

    print(f"Rows loaded: {rows_loaded}")
    print(f"Rows failed: {rows_failed}")
    print(f"Runtime: {runtime_minutes} minutes")
    print(f"Failure rate: {failure_rate:.2f}%")
    print(f"Pipeline status: {status}")
    print("-" * 40)


# Test case 1
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18
check_pipeline_health(rows_loaded, rows_failed, runtime_minutes)

# Test case 2
rows_loaded = 9500
rows_failed = 500
runtime_minutes = 15
check_pipeline_health(rows_loaded, rows_failed, runtime_minutes)

# Test case 3: low failure rate, but runtime is too high
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30
check_pipeline_health(rows_loaded, rows_failed, runtime_minutes)