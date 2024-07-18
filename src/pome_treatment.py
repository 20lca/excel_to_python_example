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

def POMEFromPressHydroCycloneSteriliser(TotalProcessedFFB,
                                        POMEClarificationSteriliserCondensate):

    # E29
    if TotalProcessedFFB > 0:
        result = POMEClarificationSteriliserCondensate
    else:
        result = 0

    return result

def POMEClarificationSteriliserCondensate():

    return 0.53 + 0.12

