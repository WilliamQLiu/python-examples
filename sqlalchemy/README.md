QueueMetrics SSIS Package

1.) Execute SQL Task to Drop Copy Table
    USE LifeNetDW 
    DROP TABLE QueueMetricsCopy
2.) Execute SQL Task to Create Copy Table
    USE LifeNetDW 
    SELECT * INTO QueueMetricsCopy
    FROM QueueMetrics
3.) Execute SQL Task to Delete Import Tables
    USE LifeNetDW 
    DELETE FROM q1import 
    DELETE FROM q2import
4.) Data Flow Task - QueueMetrics Calls Abandoned
    Take QueueMetrics - CallsKO (Abandoned)
    Do Data Convert for Table Q1
    Take Converted Data and Map to SQL Database (dbo.q1import)
4.) Data Flow Task - QueueMetrics Calls Answered
    Take QueueMetrics - CallsKO (Abandoned)
    Do Data Convert for Table Q2
    Take Converted Data and Map to SQL Database (dbo.q2import)
5.) Execute SQL Task to Update Abandon and Answer Status
    USE LifeNetDW
    UPDATE q1import
    SET CALLKO_reason = 'Abandon'
    WHERE CALLKO_reason = 'A'
    UPDATE q2import
    SET CALLOK_reason = 'Answer'
6.) Execute SQL Task to Update Nulls to 0's
    Update [LifeNetDW].[dbo].[q1import] 
    SET [CALLKO_from]= NULL 
    WHERE IsNumeric(CALLKO_from) = 0

    Update [LifeNetDW].[dbo].[q2import] 
    SET [CALLOK_from]= NULL 
    WHERE IsNumeric(CALLOK_from) = 0
7.) Execute SQL Task to drop QueueMetricsImportNewCalls Table
    USE LifeNetDW

    DROP TABLE QueueMetricsImportNewCalls
8.) Execute SQL Task to Convert Times
    Use LifeNetDW
    SELECT dateadd(second,CALLKO_callid - 18000,'1970-1-1') as 'CallTime'
        ,Str(CALLKO_from,10,0) as 'Caller'
        ,CALLKO_waitLen AS 'Wait'
        ,NULL as 'Duration'
        ,CALLKO_reason as 'Disconnection'
        ,CALLko_ivr as 'IVRName'
        ,CALLKO_dnis as 'DNISNumber'
        ,NULL as 'DNISName'
        ,NULL as 'AgentID'
    into QueueMetricsImportNewCalls
    From [q1import] 
    Union 
    SELECT dateadd(second,CALLOK_callid - 18000,'1970-1-1') as 'CallTime',
        Str(CALLOK_from,10,0) as 'Caller'
        ,CALLOK_waitLen AS 'Wait'
        ,CALLOK_callLen as 'Duration'
        ,CALLOK_reason as 'Disconnection'
        ,CALLOK_ivr as 'IVRName'
        ,CALLOK_dnis as 'DNISNumber'
        , NULL as 'DNISName'
        ,CALLOK_agent as 'AgentID'
    From [q2import]
9.) Data Flow Task - Copy QueueMetricsImportNewCalls Table to QueueMetrics Table
    Take dbo.QueueMetricsImportNewCalls
    Do data conversion
    Load data to [dbo].[QueueMetrics]
