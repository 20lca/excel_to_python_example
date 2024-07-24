"""POME treatment
This module calculates emissions from two alternative treatment processes for
POME, 'biogas' (anaerobic digestion) or 

"""

def TotalShareBiogasCaptured(ShareBiogasCaptureOpenFlare,
                             ShareBiogasCaptureEnclosedFlare,
                             ShareBiogasCaptureBiogasEngine,
                             ShareBiogasCaptureFuelSubstituteInOilMillBoiler,
                             ShareBiogasCaptureFuelSubstituteFuelOil,):

    total = (ShareBiogasCaptureOpenFlare + ShareBiogasCaptureEnclosedFlare + 
             ShareBiogasCaptureBiogasEngine + 
             ShareBiogasCaptureFuelSubstituteInOilMillBoiler + 
             ShareBiogasCaptureFuelSubstituteFuelOil)

    return total

def CapturedMethaneOpenFlare(ProcessedFFB,TotalShareBiogasCaptured,
                             CapturedMethaneApplied,
                             ShareBiogasCaptureOpenFlare,
                            ):
    # cell E16    

    try:
        open_flare = (CapturedMethaneApplied * ProcessedFFB / 1000 
                      * ShareBiogasCaptureOpenFlare / TotalShareBiogasCaptured)
    except:
        open_flare = 0

    return open_flare

def CapturedMethaneEnclosedFlare(ProcessedFFB,TotalShareBiogasCaptured,
                                 CapturedMethaneApplied,
                                 ShareBiogasCaptureEnclosedFlare,):
    # cell E17

    try:
        enclosed_flare = (CapturedMethaneApplied * ProcessedFFB / 1000 
                      * ShareBiogasCaptureEnclosedFlare / TotalShareBiogasCaptured)
    except:
        enclosed_flare = 0

    return enclosed_flare

def CapturedMethaneBiogasEngine(ProcessedFFB,TotalShareBiogasCaptured,
                                CapturedMethaneApplied,
                                ShareBiogasCaptureBiogasEngine,):
    # cell E18

    try:
        biogas_engine = (CapturedMethaneApplied * ProcessedFFB / 1000 
                      * ShareBiogasCaptureBiogasEngine / TotalShareBiogasCaptured)
    except:
        biogas_engine = 0

    return biogas_engine

def CapturedMethaneFuelSubstituteInOilMillBoiler(ProcessedFFB,
    TotalShareBiogasCaptured,CapturedMethaneApplied,ShareBiogasCaptureFuelSubstituteInOilMillBoiler,):

    # E19
    try:
        subst_oilmillboiler = (CapturedMethaneApplied * ProcessedFFB / 1000 
        * ShareBiogasCaptureFuelSubstituteInOilMillBoiler / TotalShareBiogasCaptured)
    except:
        subst_oilmillboiler = 0

    return subst_oilmillboiler

def CapturedMethaneFuelSubstituteFuelOil(ProcessedFFB,
    TotalShareBiogasCaptured,CapturedMethaneApplied,ShareBiogasCaptureFuelSubstituteFuelOil,):

    # E20
    try:
        subts_fueloil = (CapturedMethaneApplied * ProcessedFFB / 1000 
        * ShareBiogasCaptureFuelSubstituteFuelOil / TotalShareBiogasCaptured)
    except:
        subts_fueloil = 0

    return subts_fueloil

def POMETreatmentCH4(ProcessedFFB,CH4EmissionsFromPOMETotal,):

    ch4 = ProcessedFFB * CH4EmissionsFromPOMETotal / 1000

    return ch4

def POMETreatmentN2O(ProcessedFFB,N2ONonMethane):

    n2o = ProcessedFFB * N2ONonMethane / 1000

    return n2o

def POMETreatmentNH3(ProcessedFFB,NH3NonMethane):

    nh3 = ProcessedFFB * NH3NonMethane / 1000

    return nh3

def POMETreatmentH2S(ProcessedFFB,H2SNonMethane):

    nh3 = ProcessedFFB * H2SNonMethane / 1000

    return nh3

def SharePOMETreatedBiogasCapture(SharePOMETreatedAnaerobicPond):

    # E27
    share = 1 - SharePOMETreatedAnaerobicPond

    return share

def POMEFromPressHydroCycloneSteriliser(ProcessedFFB,
                                        POMEClarificationSteriliserCondensate):

    # E29
    if ProcessedFFB > 0:
        result = POMEClarificationSteriliserCondensate
    else:
        result = 0

    return result

def POMEClarificationSteriliserCondensate():

    return 0.53 + 0.12

def POMEEFBPress():
    # cell 174, parameters sheet
    return 0.140

def POMEFromEFBPress(ProcessedFFB:float,POMEEFBPress:float,
                     POMEEFBPressUsed:bool)->float:
    """_summary_

    Parameters
    ----------
    ProcessedFFB : _type_
        _description_
    POMEEFBPress : _type_
        t POME / t FFB (fresh weight)
    POMEEFBPressUsed : bool
        parameter in Oil mill input, it can have the values 'yes' or 'no'

    Returns
    -------
    float
        m3 / t FFB
    """

    # NOTE: this way is not very efficient but I reproduce the excel where the
    # formula is accross different rows

    if (ProcessedFFB > 0) and POMEEFBPressUsed:
        result = POMEEFBPress
    else:
        result = 0

    return result

def POMEFromDecanter(ProcessedFFB:float,POMEDecanterUsed:bool,
                     POMEDecanterSludge:float)->float:
    """_summary_

    Parameters
    ----------
    ProcessedFFB : float
        _description_
    POMEDecanterUsed : bool
        it seems to be if a decanter is used or not. D17 in Oil milss consolidate
    POMEDecanterSludge : float
        (t POME / t FFB) # E179 in 'Parameters'

    Returns
    -------
    float
        _description_
    """

    if (ProcessedFFB > 0) and POMEDecanterUsed:
        result = POMEDecanterSludge
    else:
        result = 0

    return result

def POMETotal(POMEFromEFBPress,POMEFromDecanter,
              POMEFromPressHydroCycloneSteriliser):
    
    total  = (POMEFromEFBPress + POMEFromDecanter + 
              POMEFromPressHydroCycloneSteriliser)
    
    return total

## functions related to COD of POME before treatment

def POMECODBeforeTreatment(POMEFromEFBPressCOD,POMEFromDecanterCOD,
                           POMEFromPressHydroCycloneSteriliserCOD,
                           POMEFromEFBPress,POMEFromDecanter,
                           POMEFromPressHydroCycloneSteriliser,
                           POMETotal,CODPOMEBeforeDigestion):
    
    # we put together some formulas because intermediate parameters are not used
    # for anything else E40

    cod = (POMEFromEFBPressCOD * POMEFromEFBPress 
           + POMEFromPressHydroCycloneSteriliserCOD * POMEFromPressHydroCycloneSteriliser
           + POMEFromDecanterCOD * POMEFromDecanter)

    try:
        cod_per_pome = cod / POMETotal # kg / m3
    except ZeroDivisionError:
        cod_per_pome = 0

    # NOTE: here whay they meant is that if COD before digestion is reported
    # then use the value. In excel an empty cell is understood as 0. that's why
    # they check if it's bigger than 0... 

    if CODPOMEBeforeDigestion > 0:
        result = CODPOMEBeforeDigestion / 1000 # reported in ppm
    else:
        result = cod_per_pome

    return result

def CODOutCODInPondSystem():
    # calculated in Parameters E183
    return 2.941/52

def CODOutCODInDigester():
    # Parameters E184
    return 10/52

def POMECODAfterPondTreatment(POMECODBeforeTreatment,CODOutCODInPondSystem,
                              CODPondSystemReported):
    # oil mill calc E45 . Pond system    
    
    if CODPondSystemReported > 0:
        result = CODPondSystemReported / 1000
    else:
        result = POMECODBeforeTreatment * CODOutCODInPondSystem

    return result

def POMECODAfterBiogasDigesterTreatment(POMECODBeforeTreatment,
                                        CODOutCODInDigester,CODDigesterReported):
    
    if CODDigesterReported > 0:
        result = CODDigesterReported / 1000
    else:
        result = POMECODBeforeTreatment * CODOutCODInDigester

    return result

def PondSystemCODReduction(POMECODAfterPondTreatment,POMECODBeforeTreatment,
                           SharePOMETreatedBiogasCapture,):
    # 
    result = ((POMECODBeforeTreatment - POMECODAfterPondTreatment) 
              * (1-SharePOMETreatedBiogasCapture))
    
    return result

def POMEAppliedToLandCODReduction(POMECODAfterPondTreatment,
                                  SharePOMETreatedAnaerobicPond):
    
    return POMECODAfterPondTreatment * SharePOMETreatedAnaerobicPond

def CH4PondSystem(PondSystemCODReduction,B0,MCFAnaerobicPond):

    ch4 = PondSystemCODReduction * B0 * MCFAnaerobicPond

    return ch4

def CH4FromPOMEAppliedToLand(POMEAppliedToLandCODReduction,B0,
                             MFCPOMEAppliedToLand):

    ch4 = POMEAppliedToLandCODReduction * B0 * MFCPOMEAppliedToLand

    return ch4

def CH4FromPOMEDischargedRiver(POMEAppliedToLandCODReduction,B0,
                               MFCPOMEDischargedRiver):

    ch4 = POMEAppliedToLandCODReduction * B0 * MFCPOMEDischargedRiver

    return ch4

## biogas digester system






