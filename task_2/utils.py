def process_data(data, row):
    """
    Helper function to process data from raw data file and format them to the correct structure required

    Args:
        data (list): List of data
        row (pandas.Series): Data row/record
    """
    data.append(
        {
            "insuree#": int(row["insuree#"]),
            "gender": row["gender"],
            "is45OrOlder": row["is45OrOlder"] == 1,
            "isMarried": row["isMarried"] == "Yes",
            "hasKids": row["hasKids"] == "Yes",
            "insuredMonths": int(row["insuredMonths"]),
            "termLifeInsurance": {
                "hasPolicy": row["termLifeInsurance"] == "Yes",
                "hasMultiplePolicies": row["multipleTermLifePolicies"] == "Yes",
            },
            "healthInsurance": {
                "hasPolicy": row["termLifeInsurance"] != "No",
                "riders": row["healthRiders"].split(",") if type(row["healthRiders"]) == str else [],
            },
            "premiumFrequency": int(row["premiumFrequency"]) if type(row["premiumFrequency"]) == str else 0,
            "eStatements": row["eStatements"] == "Yes",
            "monthlyPremium": float(row["monthlyPremium"].replace(',', '')) if row["monthlyPremium"] != " " else 0,
            "totalPremium": float(row["totalPremium"].replace(',', '')) if row["totalPremium"] != " " else 0,
            "renewal": row["renewal"] == "Y"
        }
    )