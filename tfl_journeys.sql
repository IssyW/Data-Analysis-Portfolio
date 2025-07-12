SELECT 
    DATE(CONCAT(
        SUBSTRING(CAST(TravelDate AS STRING), 1, 4), "-", 
        SUBSTRING(CAST(TravelDate AS STRING), 5, 2), "-",
        SUBSTRING(CAST(TravelDate AS STRING), 7, 2))) AS TravelDate, 
    DayOfWeek, 
    TubeJourneyCount,
    BusJourneyCount

FROM `cleaning.journeys`;
