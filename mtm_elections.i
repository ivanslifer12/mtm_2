%module mtm_elections
%include "typemaps.i"
%{
#include "mtm_elections.h"
typedef struct mtm_elections_t* MtmElections;
typedef int (*RankFunc)(MtmElections, int, void*);
%}
typedef struct mtm_elections_t* MtmElections;
typedef int (*RankFunc)(MtmElections, int, void*);
typedef enum mtmElectionsResult_t{
        MTM_ELECTIONS_MEMORY_ERROR,
        MTM_ELECTIONS_NULL_ARGUMENT,
        MTM_ELECTIONS_ILLEGAL_ID,
        MTM_ELECTIONS_ILLEGAL_AGE,
        MTM_ELECTIONS_ILLEGAL_PRIORITY,
        MTM_ELECTIONS_ILLEGAL_NUMBER_OF_YEARS,
        MTM_ELECTIONS_CITIZEN_ALREADY_EXISTS,
        MTM_ELECTIONS_CITIZEN_DOES_NOT_EXIST,
        MTM_ELECTIONS_CANDIDATE_ALREADY_EXISTS,
        MTM_ELECTIONS_CANDIDATE_DOES_NOT_EXIST,
        MTM_ELECTIONS_CITY_ALREADY_EXISTS,
        MTM_ELECTIONS_CITY_DOES_NOT_EXIST,
        MTM_ELECTIONS_NOT_SAME_CITY,
        MTM_ELECTIONS_ALREADY_SUPPORTED,
        MTM_ELECTIONS_NOT_SUPPORTED,
        MTM_ELECTIONS_CAN_NOT_SUPPORT,
        MTM_ELECTIONS_MUST_SUPPORT,
        MTM_ELECTIONS_AGE_NOT_APPROPRIATE,
        MTM_ELECTIONS_PRIORITY_EXISTS,
        MTM_ELECTIONS_NO_CANDIDATES_IN_CITY,
        MTM_ELECTIONS_FILE_ERROR,
        MTM_ELECTIONS_SUCCESS
}MtmElectionsResult;
MtmElections mtmElectionsCreate(MtmElections mtmElections);
MtmElections mtmElectionsAddCity(MtmElections mtmElections, int citizenId, int* cityId);
MtmElections mtmElectionsAddCitizen(MtmElections mtmElections, const char* citizenName,
		int citizenId, int citizenAge, int yearsOfEducation, int cityId);
MtmElections mtmElectionsAddCandidate(MtmElections mtmElections, int candidateId, int cityId);
MtmElections mtmElectionsSupportCandidate(MtmElections mtmElections, int citizenId, int candidateId, int priority);
MtmElections mtmElectionsMayorOfCity(MtmElections mtmElections, const char* cityName, int cityId);
MtmElections mtmElectionsDestroy(MtmElections mtmElections);




UniqueOrderedList mtmElectionsPerformElections(MtmElections mtmElections, RankFunc rank, void* auxilaryData, const char* filename);

%inline %{
extern MtmElectionsResult mtmElectionsMayorOfCity(MtmElections mtmElections, int cityId, int* OUTPUT, const char* filename);
%}



