-- =====================================================
-- A/B Testing Data Deaggregation Script
-- Purpose: Convert aggregated session count data to individual session records
-- Author: Marc Dutton
-- Date: December 2024
-- =====================================================

WITH r1 AS (
    -- Base case: Initial rows with session_count as it is
    SELECT 
        date_id, 
        group_id, 
        session_result, 
        CAST(session_count AS INT) AS session_count 
    FROM dbo.test -- table name on my local host in SSMS

    UNION ALL -- this keeps duplicate data i.e Group A session result 1 on date id

    -- Recursive case: Decrease session_count by 1 until session_count = 1
    SELECT 
        date_id, 
        group_id, 
        session_result, 
        CAST(session_count - 1 AS INT) AS session_count
    FROM r1
    WHERE session_count > 1
)

-- Final select from the recursive CTE
SELECT 
    date_id, 
    group_id, 
    session_result 
FROM r1
OPTION (MAXRECURSION 0); -- Allow for unlimited recursion

-- =====================================================
-- Sample Output Verification
-- =====================================================

-- Sample query to verify results (TOP 10 for testing)
-- SELECT TOP 10 date_id, group_id, session_result 
-- FROM r1
-- OPTION (MAXRECURSION 0);

/*
Expected sample results:
date_id	        group_id	session_result
25/06/2018      A	        0
25/06/2018      B	        0
25/06/2018      A	        1
25/06/2018      B	        1
26/06/2018      A	        0
26/06/2018      B	        0
26/06/2018      A	        1
26/06/2018      B	        1
27/06/2018      A	        0
27/06/2018      B	        0
*/
