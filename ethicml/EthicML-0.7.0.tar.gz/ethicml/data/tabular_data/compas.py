"""Class to describe features of the Compas dataset."""
from dataclasses import dataclass
from enum import Enum
from typing import Union

from ..dataset import LoadableDataset
from ..util import LabelSpec, flatten_dict, simple_spec

__all__ = ["Compas", "CompasSplits", "compas"]


class CompasSplits(Enum):
    """Available dataset splits for the COMPAS dataset."""

    SEX = "Sex"
    RACE = "Race"
    RACE_SEX = "Race-Sex"
    CUSTOM = "Custom"


def compas(
    split: Union[CompasSplits, str] = "Sex",
    discrete_only: bool = False,
    invert_s: bool = False,
) -> "Compas":
    """Compas (or ProPublica) dataset."""
    return Compas(split=CompasSplits(split), discrete_only=discrete_only, invert_s=invert_s)


@dataclass
class Compas(LoadableDataset):
    """Compas (or ProPublica) dataset."""

    split: CompasSplits = CompasSplits.SEX

    def __post_init__(self) -> None:
        disc_feature_groups = {
            "sex": ["sex"],
            "race": ["race"],
            "two-year-recid": ["two-year-recid"],
            "age-cat": ["age-cat_25 - 45", "age-cat_Greater than 45", "age-cat_Less than 25"],
            "c-charge-degree": ["c-charge-degree_F", "c-charge-degree_M"],
            "c-charge-desc": [
                "c-charge-desc_Abuse Without Great Harm",
                "c-charge-desc_Agg Abuse Elderlly/Disabled Adult",
                "c-charge-desc_Agg Assault W/int Com Fel Dome",
                "c-charge-desc_Agg Battery Grt/Bod/Harm",
                "c-charge-desc_Agg Fleeing and Eluding",
                "c-charge-desc_Agg Fleeing/Eluding High Speed",
                "c-charge-desc_Aggr Child Abuse-Torture,Punish",
                "c-charge-desc_Aggrav Battery w/Deadly Weapon",
                "c-charge-desc_Aggrav Child Abuse-Agg Battery",
                "c-charge-desc_Aggrav Child Abuse-Causes Harm",
                "c-charge-desc_Aggrav Stalking After Injunctn",
                "c-charge-desc_Aggravated Assault",
                "c-charge-desc_Aggravated Assault W/Dead Weap",
                "c-charge-desc_Aggravated Assault W/dead Weap",
                "c-charge-desc_Aggravated Assault W/o Firearm",
                "c-charge-desc_Aggravated Assault w/Firearm",
                "c-charge-desc_Aggravated Battery",
                "c-charge-desc_Aggravated Battery (Firearm)",
                "c-charge-desc_Aggravated Battery (Firearm/Actual Possession)",
                "c-charge-desc_Aggravated Battery / Pregnant",
                "c-charge-desc_Aggravated Battery On 65/Older",
                "c-charge-desc_Aide/Abet Prostitution Lewdness",
                "c-charge-desc_Aiding Escape",
                "c-charge-desc_Alcoholic Beverage Violation-FL",
                "c-charge-desc_Armed Trafficking in Cannabis",
                "c-charge-desc_Arson in the First Degree",
                "c-charge-desc_Assault",
                "c-charge-desc_Assault Law Enforcement Officer",
                "c-charge-desc_Att Burgl Conv Occp",
                "c-charge-desc_Att Burgl Struc/Conv Dwel/Occp",
                "c-charge-desc_Att Burgl Unoccupied Dwel",
                "c-charge-desc_Att Tamper w/Physical Evidence",
                "c-charge-desc_Attempt Armed Burglary Dwell",
                "c-charge-desc_Attempted Burg/Convey/Unocc",
                "c-charge-desc_Attempted Burg/struct/unocc",
                "c-charge-desc_Attempted Deliv Control Subst",
                "c-charge-desc_Attempted Robbery  No Weapon",
                "c-charge-desc_Attempted Robbery  Weapon",
                "c-charge-desc_Battery",
                "c-charge-desc_Battery Emergency Care Provide",
                "c-charge-desc_Battery On A Person Over 65",
                "c-charge-desc_Battery On Fire Fighter",
                "c-charge-desc_Battery On Parking Enfor Speci",
                "c-charge-desc_Battery Spouse Or Girlfriend",
                "c-charge-desc_Battery on Law Enforc Officer",
                "c-charge-desc_Battery on a Person Over 65",
                "c-charge-desc_Bribery Athletic Contests",
                "c-charge-desc_Burgl Dwel/Struct/Convey Armed",
                "c-charge-desc_Burglary Assault/Battery Armed",
                "c-charge-desc_Burglary Conveyance Armed",
                "c-charge-desc_Burglary Conveyance Assault/Bat",
                "c-charge-desc_Burglary Conveyance Occupied",
                "c-charge-desc_Burglary Conveyance Unoccup",
                "c-charge-desc_Burglary Dwelling Armed",
                "c-charge-desc_Burglary Dwelling Assault/Batt",
                "c-charge-desc_Burglary Dwelling Occupied",
                "c-charge-desc_Burglary Structure Assault/Batt",
                "c-charge-desc_Burglary Structure Occupied",
                "c-charge-desc_Burglary Structure Unoccup",
                "c-charge-desc_Burglary Unoccupied Dwelling",
                "c-charge-desc_Burglary With Assault/battery",
                "c-charge-desc_Carjacking w/o Deadly Weapon",
                "c-charge-desc_Carjacking with a Firearm",
                "c-charge-desc_Carry Open/Uncov Bev In Pub",
                "c-charge-desc_Carrying A Concealed Weapon",
                "c-charge-desc_Carrying Concealed Firearm",
                "c-charge-desc_Cash Item w/Intent to Defraud",
                "c-charge-desc_Child Abuse",
                "c-charge-desc_Computer Pornography",
                "c-charge-desc_Consp Traff Oxycodone  4g><14g",
                "c-charge-desc_Conspiracy Dealing Stolen Prop",
                "c-charge-desc_Consume Alcoholic Bev Pub",
                "c-charge-desc_Contradict Statement",
                "c-charge-desc_Contribute Delinquency Of A Minor",
                "c-charge-desc_Corrupt Public Servant",
                "c-charge-desc_Counterfeit Lic Plates/Sticker",
                "c-charge-desc_Crim Attempt/Solic/Consp",
                "c-charge-desc_Crim Use of Personal ID Info",
                "c-charge-desc_Crimin Mischief Damage $1000+",
                "c-charge-desc_Criminal Mischief",
                "c-charge-desc_Criminal Mischief Damage <$200",
                "c-charge-desc_Criminal Mischief>$200<$1000",
                "c-charge-desc_Crlty Twrd Child Urge Oth Act",
                "c-charge-desc_Cruelty Toward Child",
                "c-charge-desc_Cruelty to Animals",
                "c-charge-desc_Culpable Negligence",
                "c-charge-desc_D.U.I. Serious Bodily Injury",
                "c-charge-desc_DOC/Cause Public Danger",
                "c-charge-desc_DUI - Enhanced",
                "c-charge-desc_DUI - Property Damage/Personal Injury",
                "c-charge-desc_DUI Blood Alcohol Above 0.20",
                "c-charge-desc_DUI Level 0.15 Or Minor In Veh",
                "c-charge-desc_DUI Property Damage/Injury",
                "c-charge-desc_DUI- Enhanced",
                "c-charge-desc_DUI/Property Damage/Persnl Inj",
                "c-charge-desc_DWI w/Inj Susp Lic / Habit Off",
                "c-charge-desc_DWLS Canceled Disqul 1st Off",
                "c-charge-desc_DWLS Susp/Cancel Revoked",
                "c-charge-desc_Dealing in Stolen Property",
                "c-charge-desc_Defrauding Innkeeper",
                "c-charge-desc_Defrauding Innkeeper $300/More",
                "c-charge-desc_Del 3,4 Methylenedioxymethcath",
                "c-charge-desc_Del Cannabis At/Near Park",
                "c-charge-desc_Del Cannabis For Consideration",
                "c-charge-desc_Del of JWH-250 2-Methox 1-Pentyl",
                "c-charge-desc_Deliver 3,4 Methylenediox",
                "c-charge-desc_Deliver Alprazolam",
                "c-charge-desc_Deliver Cannabis",
                "c-charge-desc_Deliver Cannabis 1000FTSch",
                "c-charge-desc_Deliver Cocaine",
                "c-charge-desc_Deliver Cocaine 1000FT Church",
                "c-charge-desc_Deliver Cocaine 1000FT Park",
                "c-charge-desc_Deliver Cocaine 1000FT School",
                "c-charge-desc_Deliver Cocaine 1000FT Store",
                "c-charge-desc_Delivery Of Drug Paraphernalia",
                "c-charge-desc_Delivery of 5-Fluoro PB-22",
                "c-charge-desc_Delivery of Heroin",
                "c-charge-desc_Depriv LEO of Protect/Communic",
                "c-charge-desc_Disorderly Conduct",
                "c-charge-desc_Disorderly Intoxication",
                "c-charge-desc_Disrupting School Function",
                "c-charge-desc_Drivg While Lic Suspd/Revk/Can",
                "c-charge-desc_Driving License Suspended",
                "c-charge-desc_Driving Under The Influence",
                "c-charge-desc_Driving While License Revoked",
                "c-charge-desc_Escape",
                "c-charge-desc_Exhibition Weapon School Prop",
                "c-charge-desc_Expired DL More Than 6 Months",
                "c-charge-desc_Exposes Culpable Negligence",
                "c-charge-desc_Extradition/Defendants",
                "c-charge-desc_Fabricating Physical Evidence",
                "c-charge-desc_Fail Register Vehicle",
                "c-charge-desc_Fail Sex Offend Report Bylaw",
                "c-charge-desc_Fail To Obey Police Officer",
                "c-charge-desc_Fail To Redeliv Hire/Leas Prop",
                "c-charge-desc_Failure To Pay Taxi Cab Charge",
                "c-charge-desc_Failure To Return Hired Vehicle",
                "c-charge-desc_False 911 Call",
                "c-charge-desc_False Bomb Report",
                "c-charge-desc_False Imprisonment",
                "c-charge-desc_False Info LEO During Invest",
                "c-charge-desc_False Motor Veh Insurance Card",
                "c-charge-desc_False Name By Person Arrest",
                "c-charge-desc_False Ownership Info/Pawn Item",
                "c-charge-desc_Falsely Impersonating Officer",
                "c-charge-desc_Fel Drive License Perm Revoke",
                "c-charge-desc_Felon in Pos of Firearm or Amm",
                "c-charge-desc_Felony Batt(Great Bodily Harm)",
                "c-charge-desc_Felony Battery",
                "c-charge-desc_Felony Battery (Dom Strang)",
                "c-charge-desc_Felony Battery w/Prior Convict",
                "c-charge-desc_Felony Committing Prostitution",
                "c-charge-desc_Felony DUI (level 3)",
                "c-charge-desc_Felony DUI - Enhanced",
                "c-charge-desc_Felony Driving While Lic Suspd",
                "c-charge-desc_Felony Petit Theft",
                "c-charge-desc_Felony/Driving Under Influence",
                "c-charge-desc_Fighting/Baiting Animals",
                "c-charge-desc_Fleeing Or Attmp Eluding A Leo",
                "c-charge-desc_Fleeing or Eluding a LEO",
                "c-charge-desc_Forging Bank Bills/Promis Note",
                "c-charge-desc_Fraudulent Use of Credit Card",
                "c-charge-desc_Grand Theft (Motor Vehicle)",
                "c-charge-desc_Grand Theft Dwell Property",
                "c-charge-desc_Grand Theft Firearm",
                "c-charge-desc_Grand Theft in the 1st Degree",
                "c-charge-desc_Grand Theft in the 3rd Degree",
                "c-charge-desc_Grand Theft of a Fire Extinquisher",
                "c-charge-desc_Grand Theft of the 2nd Degree",
                "c-charge-desc_Grand Theft on 65 Yr or Older",
                "c-charge-desc_Harass Witness/Victm/Informnt",
                "c-charge-desc_Harm Public Servant Or Family",
                "c-charge-desc_Hiring with Intent to Defraud",
                "c-charge-desc_Imperson Public Officer or Emplyee",
                "c-charge-desc_Interfere W/Traf Cont Dev RR",
                "c-charge-desc_Interference with Custody",
                "c-charge-desc_Intoxicated/Safety Of Another",
                "c-charge-desc_Introduce Contraband Into Jail",
                "c-charge-desc_Issuing a Worthless Draft",
                "c-charge-desc_Kidnapping / Domestic Violence",
                "c-charge-desc_Lease For Purpose Trafficking",
                "c-charge-desc_Leave Acc/Attend Veh/More $50",
                "c-charge-desc_Leave Accd/Attend Veh/Less $50",
                "c-charge-desc_Leaving Acc/Unattended Veh",
                "c-charge-desc_Leaving the Scene of Accident",
                "c-charge-desc_Lewd Act Presence Child 16-",
                "c-charge-desc_Lewd or Lascivious Molestation",
                "c-charge-desc_Lewd/Lasc Battery Pers 12+/<16",
                "c-charge-desc_Lewd/Lasc Exhib Presence <16yr",
                "c-charge-desc_Lewd/Lasciv Molest Elder Persn",
                "c-charge-desc_Lewdness Violation",
                "c-charge-desc_License Suspended Revoked",
                "c-charge-desc_Littering",
                "c-charge-desc_Live on Earnings of Prostitute",
                "c-charge-desc_Lve/Scen/Acc/Veh/Prop/Damage",
                "c-charge-desc_Manage Busn W/O City Occup Lic",
                "c-charge-desc_Manslaughter W/Weapon/Firearm",
                "c-charge-desc_Manufacture Cannabis",
                "c-charge-desc_Misuse Of 911 Or E911 System",
                "c-charge-desc_Money Launder 100K or More Dols",
                "c-charge-desc_Murder In 2nd Degree W/firearm",
                "c-charge-desc_Murder in the First Degree",
                "c-charge-desc_Neglect Child / Bodily Harm",
                "c-charge-desc_Neglect Child / No Bodily Harm",
                "c-charge-desc_Neglect/Abuse Elderly Person",
                "c-charge-desc_Obstruct Fire Equipment",
                "c-charge-desc_Obstruct Officer W/Violence",
                "c-charge-desc_Obtain Control Substance By Fraud",
                "c-charge-desc_Offer Agree Secure For Lewd Act",
                "c-charge-desc_Offer Agree Secure/Lewd Act",
                "c-charge-desc_Offn Against Intellectual Prop",
                "c-charge-desc_Open Carrying Of Weapon",
                "c-charge-desc_Oper Motorcycle W/O Valid DL",
                "c-charge-desc_Operating W/O Valid License",
                "c-charge-desc_Opert With Susp DL 2nd Offens",
                "c-charge-desc_PL/Unlaw Use Credit Card",
                "c-charge-desc_Petit Theft",
                "c-charge-desc_Petit Theft $100- $300",
                "c-charge-desc_Pos Cannabis For Consideration",
                "c-charge-desc_Pos Cannabis W/Intent Sel/Del",
                "c-charge-desc_Pos Methylenedioxymethcath W/I/D/S",
                "c-charge-desc_Poss 3,4 MDMA (Ecstasy)",
                "c-charge-desc_Poss Alprazolam W/int Sell/Del",
                "c-charge-desc_Poss Anti-Shoplifting Device",
                "c-charge-desc_Poss Cntrft Contr Sub w/Intent",
                "c-charge-desc_Poss Cocaine/Intent To Del/Sel",
                "c-charge-desc_Poss Contr Subst W/o Prescript",
                "c-charge-desc_Poss Counterfeit Payment Inst",
                "c-charge-desc_Poss Drugs W/O A Prescription",
                "c-charge-desc_Poss F/Arm Delinq",
                "c-charge-desc_Poss Firearm W/Altered ID#",
                "c-charge-desc_Poss Meth/Diox/Meth/Amp (MDMA)",
                "c-charge-desc_Poss Of 1,4-Butanediol",
                "c-charge-desc_Poss Of Controlled Substance",
                "c-charge-desc_Poss Of RX Without RX",
                "c-charge-desc_Poss Oxycodone W/Int/Sell/Del",
                "c-charge-desc_Poss Pyrrolidinobutiophenone",
                "c-charge-desc_Poss Pyrrolidinovalerophenone",
                "c-charge-desc_Poss Pyrrolidinovalerophenone W/I/D/S",
                "c-charge-desc_Poss Similitude of Drivers Lic",
                "c-charge-desc_Poss Tetrahydrocannabinols",
                "c-charge-desc_Poss Unlaw Issue Driver Licenc",
                "c-charge-desc_Poss Unlaw Issue Id",
                "c-charge-desc_Poss Wep Conv Felon",
                "c-charge-desc_Poss of Cocaine W/I/D/S 1000FT Park",
                "c-charge-desc_Poss of Firearm by Convic Felo",
                "c-charge-desc_Poss of Methylethcathinone",
                "c-charge-desc_Poss/Sell/Del Cocaine 1000FT Sch",
                "c-charge-desc_Poss/Sell/Del/Man Amobarbital",
                "c-charge-desc_Poss/pur/sell/deliver Cocaine",
                "c-charge-desc_Poss3,4 Methylenedioxymethcath",
                "c-charge-desc_Posses/Disply Susp/Revk/Frd DL",
                "c-charge-desc_Possess Cannabis 1000FTSch",
                "c-charge-desc_Possess Cannabis/20 Grams Or Less",
                "c-charge-desc_Possess Controlled Substance",
                "c-charge-desc_Possess Countrfeit Credit Card",
                "c-charge-desc_Possess Drug Paraphernalia",
                "c-charge-desc_Possess Mot Veh W/Alt Vin #",
                "c-charge-desc_Possess Tobacco Product Under 18",
                "c-charge-desc_Possess Weapon On School Prop",
                "c-charge-desc_Possess w/I/Utter Forged Bills",
                "c-charge-desc_Possession Burglary Tools",
                "c-charge-desc_Possession Child Pornography",
                "c-charge-desc_Possession Firearm School Prop",
                "c-charge-desc_Possession Of 3,4Methylenediox",
                "c-charge-desc_Possession Of Alprazolam",
                "c-charge-desc_Possession Of Amphetamine",
                "c-charge-desc_Possession Of Anabolic Steroid",
                "c-charge-desc_Possession Of Buprenorphine",
                "c-charge-desc_Possession Of Carisoprodol",
                "c-charge-desc_Possession Of Clonazepam",
                "c-charge-desc_Possession Of Cocaine",
                "c-charge-desc_Possession Of Diazepam",
                "c-charge-desc_Possession Of Fentanyl",
                "c-charge-desc_Possession Of Heroin",
                "c-charge-desc_Possession Of Methamphetamine",
                "c-charge-desc_Possession Of Paraphernalia",
                "c-charge-desc_Possession Of Phentermine",
                "c-charge-desc_Possession of Alcohol Under 21",
                "c-charge-desc_Possession of Benzylpiperazine",
                "c-charge-desc_Possession of Butylone",
                "c-charge-desc_Possession of Cannabis",
                "c-charge-desc_Possession of Cocaine",
                "c-charge-desc_Possession of Codeine",
                "c-charge-desc_Possession of Ethylone",
                "c-charge-desc_Possession of Hydrocodone",
                "c-charge-desc_Possession of Hydromorphone",
                "c-charge-desc_Possession of LSD",
                "c-charge-desc_Possession of Methadone",
                "c-charge-desc_Possession of Morphine",
                "c-charge-desc_Possession of Oxycodone",
                "c-charge-desc_Possession of XLR11",
                "c-charge-desc_Principal In The First Degree",
                "c-charge-desc_Prostitution",
                "c-charge-desc_Prostitution/Lewd Act Assignation",
                "c-charge-desc_Prostitution/Lewdness/Assign",
                "c-charge-desc_Prowling/Loitering",
                "c-charge-desc_Purchase Cannabis",
                "c-charge-desc_Purchase/P/W/Int Cannabis",
                "c-charge-desc_Reckless Driving",
                "c-charge-desc_Refuse Submit Blood/Breath Test",
                "c-charge-desc_Refuse to Supply DNA Sample",
                "c-charge-desc_Resist Officer w/Violence",
                "c-charge-desc_Resist/Obstruct W/O Violence",
                "c-charge-desc_Retail Theft $300 1st Offense",
                "c-charge-desc_Retail Theft $300 2nd Offense",
                "c-charge-desc_Ride Tri-Rail Without Paying",
                "c-charge-desc_Robbery / No Weapon",
                "c-charge-desc_Robbery / Weapon",
                "c-charge-desc_Robbery Sudd Snatch No Weapon",
                "c-charge-desc_Robbery W/Deadly Weapon",
                "c-charge-desc_Robbery W/Firearm",
                "c-charge-desc_Sale/Del Cannabis At/Near Scho",
                "c-charge-desc_Sale/Del Counterfeit Cont Subs",
                "c-charge-desc_Sel/Pur/Mfr/Del Control Substa",
                "c-charge-desc_Sell or Offer for Sale Counterfeit Goods",
                "c-charge-desc_Sell/Man/Del Pos/w/int Heroin",
                "c-charge-desc_Sex Batt Faml/Cust Vict 12-17Y",
                "c-charge-desc_Sex Battery Deft 18+/Vict 11-",
                "c-charge-desc_Sex Offender Fail Comply W/Law",
                "c-charge-desc_Sexual Battery / Vict 12 Yrs +",
                "c-charge-desc_Sexual Performance by a Child",
                "c-charge-desc_Shoot In Occupied Dwell",
                "c-charge-desc_Shoot Into Vehicle",
                "c-charge-desc_Simulation of Legal Process",
                "c-charge-desc_Solic to Commit Battery",
                "c-charge-desc_Solicit Deliver Cocaine",
                "c-charge-desc_Solicit Purchase Cocaine",
                "c-charge-desc_Solicit To Deliver Cocaine",
                "c-charge-desc_Solicitation On Felony 3 Deg",
                "c-charge-desc_Soliciting For Prostitution",
                "c-charge-desc_Sound Articles Over 100",
                "c-charge-desc_Stalking",
                "c-charge-desc_Stalking (Aggravated)",
                "c-charge-desc_Strong Armed  Robbery",
                "c-charge-desc_Structuring Transactions",
                "c-charge-desc_Susp Drivers Lic 1st Offense",
                "c-charge-desc_Tamper With Victim",
                "c-charge-desc_Tamper With Witness",
                "c-charge-desc_Tamper With Witness/Victim/CI",
                "c-charge-desc_Tampering With Physical Evidence",
                "c-charge-desc_Tampering with a Victim",
                "c-charge-desc_Theft/To Deprive",
                "c-charge-desc_Threat Public Servant",
                "c-charge-desc_Throw Deadly Missile Into Veh",
                "c-charge-desc_Throw In Occupied Dwell",
                "c-charge-desc_Throw Missile Into Pub/Priv Dw",
                "c-charge-desc_Traff In Cocaine <400g>150 Kil",
                "c-charge-desc_Traffic Counterfeit Cred Cards",
                "c-charge-desc_Traffick Amphetamine 28g><200g",
                "c-charge-desc_Traffick Oxycodone     4g><14g",
                "c-charge-desc_Trans/Harm/Material to a Minor",
                "c-charge-desc_Trespass On School Grounds",
                "c-charge-desc_Trespass Other Struct/Conve",
                "c-charge-desc_Trespass Private Property",
                "c-charge-desc_Trespass Property w/Dang Weap",
                "c-charge-desc_Trespass Struct/Conveyance",
                "c-charge-desc_Trespass Structure w/Dang Weap",
                "c-charge-desc_Trespass Structure/Conveyance",
                "c-charge-desc_Trespassing/Construction Site",
                "c-charge-desc_Tresspass Struct/Conveyance",
                "c-charge-desc_Tresspass in Structure or Conveyance",
                "c-charge-desc_Unauth C/P/S Sounds>1000/Audio",
                "c-charge-desc_Unauth Poss ID Card or DL",
                "c-charge-desc_Unauthorized Interf w/Railroad",
                "c-charge-desc_Unl/Disturb Education/Instui",
                "c-charge-desc_Unlaw Lic Use/Disply Of Others",
                "c-charge-desc_Unlaw LicTag/Sticker Attach",
                "c-charge-desc_Unlaw Use False Name/Identity",
                "c-charge-desc_Unlawful Conveyance of Fuel",
                "c-charge-desc_Unlicensed Telemarketing",
                "c-charge-desc_Use Computer for Child Exploit",
                "c-charge-desc_Use Of 2 Way Device To Fac Fel",
                "c-charge-desc_Use Scanning Device to Defraud",
                "c-charge-desc_Use of Anti-Shoplifting Device",
                "c-charge-desc_Uttering Forged Bills",
                "c-charge-desc_Uttering Forged Credit Card",
                "c-charge-desc_Uttering Worthless Check +$150",
                "c-charge-desc_Uttering a Forged Instrument",
                "c-charge-desc_Video Voyeur-<24Y on Child >16",
                "c-charge-desc_Viol Injunct Domestic Violence",
                "c-charge-desc_Viol Injunction Protect Dom Vi",
                "c-charge-desc_Viol Pretrial Release Dom Viol",
                "c-charge-desc_Viol Prot Injunc Repeat Viol",
                "c-charge-desc_Violation License Restrictions",
                "c-charge-desc_Violation Of Boater Safety Id",
                "c-charge-desc_Violation of Injunction Order/Stalking/Cyberstalking",
                "c-charge-desc_Voyeurism",
                "c-charge-desc_arrest case no charge",
            ],
        }
        discrete_features = flatten_dict(disc_feature_groups)

        continuous_features = [
            "age-num",
            "juv-fel-count",
            "juv-misd-count",
            "juv-other-count",
            "priors-count",
        ]

        sens_attr_spec: Union[str, LabelSpec]
        if self.split is CompasSplits.SEX:
            sens_attr_spec = "sex"
            s_prefix = ["sex"]
            class_label_spec = "two-year-recid"
            class_label_prefix = ["two-year-recid"]
        elif self.split is CompasSplits.RACE:
            sens_attr_spec = "race"
            s_prefix = ["race"]
            class_label_spec = "two-year-recid"
            class_label_prefix = ["two-year-recid"]
        elif self.split is CompasSplits.RACE_SEX:
            sens_attr_spec = simple_spec({"sex": ["sex"], "race": ["race"]})
            s_prefix = ["race", "sex"]
            class_label_spec = "two-year-recid"
            class_label_prefix = ["two-year-recid"]
        elif self.split is CompasSplits.CUSTOM:
            sens_attr_spec = ""
            s_prefix = []
            class_label_spec = ""
            class_label_prefix = []
        else:
            raise NotImplementedError

        super().__init__(
            name=f"Compas {self.split.value}",
            num_samples=6167,
            filename_or_path="compas-recidivism.csv",
            features=discrete_features + continuous_features,
            cont_features=continuous_features,
            s_prefix=s_prefix,
            sens_attr_spec=sens_attr_spec,
            class_label_prefix=class_label_prefix,
            class_label_spec=class_label_spec,
            discrete_only=self.discrete_only,
            discrete_feature_groups=disc_feature_groups,
        )
