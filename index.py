# Composite Usefulness Score Calculator for Languages
# (Values are approximate estimates based on the provided data.)

# 1. Data for Languages
# Each language is assigned six metrics:
#   N: Total speakers (in millions)
#   P: Passport strength (an approximate score)
#   C: Number of countries where the language is official (or de facto)
#   G: Combined GDP (in millions US$) for the countries where it is official
#   T: International tourist arrivals (in millions) for one of the key official countries
#   I: Cultural influence score (an approximate average from available rankings)
languages_data = {
    "English": {
        "N": 1515,      # 1.515 billion speakers
        "P": 190,       # many official countries have high‐ranking passports (e.g. UK, Australia, Singapore)
        "C": 59,        # 55 official + 4 de facto
        "G": 38000000,  # sum approximated from USA, UK, Canada, Australia, etc.
        # Sum of international arrivals for the US (66.5M), UK (37.2M), and Canada (18.3M) ≈ 122.0 million
        "T": 122.0,     
        "I": 66         # average cultural influence (e.g. USA, UK, etc.)
    },
    "Mandarin Chinese": {
        "N": 1140,      # 1.14 billion speakers
        "P": 80,        # People’s Republic passport is relatively low‐scoring
        "C": 3,         # Official in China, Singapore, and Taiwan
        "G": 21000000,  # China plus smaller contributions from Singapore/Taiwan
        # China’s 2019 international arrivals (from Asia-Pacific table)
        "T": 65.7,      
        "I": 58.37     # cultural influence roughly equal to China’s score
    },
    "Hindi": {
        "N": 609,
        "P": 60,        # India’s passport is lower‐ranked
        "C": 1,         # Official mainly in India
        "G": 4271922,   # India’s GDP (IMF forecast, in millions)
        # Using India’s 2019 arrivals from Asia-Pacific data (~17.9 million)
        "T": 17.9,      
        "I": 64.14     # using India’s cultural influence rating
    },
    "Spanish": {
        "N": 560,
        "P": 150,       # mix of European (high) and Latin American (lower) passports
        "C": 20,        # roughly 15 official + 5 de facto
        "G": 5000000,   # approximate combined GDP from Spain, Mexico, Argentina, etc.
        # Spain’s 2023 arrivals from the top–10 international tourism destinations list
        "T": 85.2,      
        "I": 67        # using Spain’s cultural influence score
    },
    "Modern Standard Arabic": {
        "N": 332,
        "P": 165,       # many Arab states (e.g. UAE, Qatar) have moderate–to–high scores
        "C": 22,        # official in 22 countries
        "G": 2000000,   # rough combined GDP for the Arab world (selected key countries)
        # Using Saudi Arabia’s 2019 figure from West Asia table (~17.5 million)
        "T": 17.5,      
        "I": 56        # approximate cultural influence for the Arabic–speaking world
    },
    "French": {
        "N": 312,
        "P": 180,       # France and several other Francophone countries have strong passports
        "C": 29,        # official in 29 countries
        "G": 4000000,   # approximate combined GDP (France and selected African states)
        # France’s 2023 arrivals from the top–10 international tourism destinations list (~100 million)
        "T": 100,      
        "I": 66        # France’s cultural influence score
    },
    "Bengali": {
        "N": 278,
        "P": 30,        # Bangladesh’s passport is relatively weak
        "C": 1,         # Official mainly in Bangladesh
        "G": 500000,    # approximate GDP for Bangladesh
        "T": 0,
        "I": 50        # not featured in the cultural influence ranking; assigned a low value
    },
    "Portuguese": {
        "N": 264,
        "P": 180,       # e.g. Portugal has a high–ranking passport; Brazil’s is lower, so average is high
        "C": 10,        # official in 10 countries
        "G": 2900000,   # sum for Portugal and Brazil (approx.)
        # Using Portugal’s 2019 arrivals from the Europe table (~24.5 million)
        "T": 24.5,      
        "I": 60        # approximate cultural influence score (average of Portugal and Brazil)
    },
    "Russian": {
        "N": 255,
        "P": 100,       # Russia’s passport is moderate
        "C": 4,         # official in 4 countries
        "G": 2200000,   # Russia’s GDP (approx.)
        "T": 0,        # No corresponding top–10 international arrival data found
        "I": 60.66     # from Russia’s cultural influence score
    },
    "Urdu": {
        "N": 238,
        "P": 60,        # Pakistan’s passport is low–ranked
        "C": 1,         # Official mainly in Pakistan
        "G": 400000,    # approximate GDP for Pakistan
        "T": 0,        # No corresponding top–10 data provided
        "I": 50        # assigned a low cultural influence value
    },
    "Indonesian": {
        "N": 199,
        "P": 80,        # Indonesia’s passport is modest
        "C": 1,         # Official primarily in Indonesia
        "G": 1492618,   # Indonesia’s GDP (IMF forecast, in millions)
        # Indonesia’s 2019 arrivals from Asia-Pacific table (~15.5 million)
        "T": 15.5,      
        "I": 52       # Indonesia’s cultural influence score (from the ranking)
    },
    "Standard German": {
        "N": 134,
        "P": 192,       # Germany’s passport is one of the world’s strongest
        "C": 6,         # Official in 6 countries
        "G": 4921563,   # Germany’s GDP (in millions)
        # Germany’s 2023 arrivals from the top–10 international tourism destinations list (~34.8 million)
        "T": 34.8,      
        "I": 59.85     # Germany’s cultural influence score
    },
    "Japanese": {
        "N": 123,
        "P": 193,       # Japan’s passport score is very high
        "C": 1,         # Official only in Japan
        "G": 4389326,   # Japan’s GDP
        # Japan’s 2019 arrivals from Asia-Pacific table (~32.2 million)
        "T": 32.2,      
        "I": 61.3      # Japan’s cultural influence score
    },
    "Nigerian Pidgin": {
        "N": 121,
        "P": 50,        # Using Nigeria’s passport (which is relatively low)
        "C": 1,         # Not officially recognized but widely used in Nigeria
        "G": 500000,    # approximate GDP for Nigeria (as a proxy)
        "T": 0,        # No top–10 tourist arrival data available
        "I": 50        # assigned a lower cultural influence score
    },
    "Egyptian Arabic": {
        "N": 103,
        "P": 50,        # Egypt’s passport is low–to–moderate
        "C": 1,         # Official mainly in Egypt
        "G": 1000000,   # approximate GDP for Egypt
        # Egypt’s 2019 arrivals from the Africa table (~13.0 million)
        "T": 13.0,      
        "I": 55        # Egypt’s cultural influence score from the ranking
    },
    "Marathi": {
        "N": 99,
        "P": 60,        # as an official language in India
        "C": 1,
        "G": 4271922,   # India’s GDP (used for any language official only in India)
        # Using India’s 2019 arrivals (~17.9 million)
        "T": 17.9,      
        "I": 64.14     # India’s cultural influence
    },
    "Telugu": {
        "N": 96,
        "P": 60,
        "C": 1,
        "G": 4271922,
        # Using India’s 2019 arrivals (~17.9 million)
        "T": 17.9,      
        "I": 64.14
    },
    "Turkish": {
        "N": 90,
        "P": 152,       # Turkey’s passport is moderately high
        "C": 2,         # Official in Turkey and Cyprus
        "G": 1455413,   # Turkey’s GDP (approx.)
        # Turkey’s 2023 arrivals from the top–10 international tourism destinations list (~55.2 million)
        "T": 55.2,      
        "I": 55.55     # Turkey’s cultural influence score
    },
    "Hausa": {
        "N": 88,
        "P": 50,        # using Nigeria’s passport as a proxy
        "C": 1,
        "G": 500000,
        "T": 0,        # No top–10 tourist arrival data available
        "I": 50
    },
    "Tamil": {
        "N": 87,
        "P": 170,       # reflecting high scores from countries like Singapore
        "C": 2,         # Official in Singapore and Sri Lanka
        "G": 561725,    # Singapore’s GDP (as a proxy)
        "T": 0,        # Neither Singapore nor Sri Lanka appear in the provided top–10 data
        "I": 53       # approximate average of Singapore (~56.5) and Sri Lanka (~49.9)
    },
    "Yue Chinese": {
        "N": 87,
        "P": 185,       # Hong Kong’s passport (used as a proxy) is high–ranking
        "C": 1,
        "G": 500000,    # an approximate value for Hong Kong
        # Hong Kong’s 2019 arrivals from Asia-Pacific table (~23.8 million)
        "T": 23.8,      
        "I": 58       # assigned close to China’s cultural influence
    },
    "Swahili": {
        "N": 87,
        "P": 50,        # passports in East Africa tend to be lower
        "C": 6,         # Official in 6 countries (e.g. Kenya, Tanzania, Uganda, etc.)
        "G": 1000000,   # rough combined GDP of these countries
        # Using Tanzania’s 2019 arrivals from the Africa table (~3.65 million)
        "T": 3.65,      
        "I": 50
    },
    "Vietnamese": {
        "N": 86,
        "P": 80,        # Vietnam’s passport score is modest
        "C": 1,
        "G": 506600,    # Vietnam’s GDP (in millions)
        # Vietnam’s 2019 arrivals from Asia-Pacific table (~18.0 million)
        "T": 18.0,      
        "I": 50.43
    },
    "Tagalog": {
        "N": 83,
        "P": 60,        # the Philippines’ passport is relatively low
        "C": 1,
        "G": 507670,    # Philippines’ GDP (in millions)
        "T": 0,        # No top–10 tourist arrival data available
        "I": 51.77
    },
    "Western Punjabi": {
        "N": 82,
        "P": 60,
        "C": 1,
        "G": 400000,    # using Pakistan’s GDP as a proxy
        "T": 0,        # No top–10 tourist arrival data available
        "I": 50
    },
    "Korean": {
        "N": 81,
        "P": 180,       # South Korea’s passport is very strong
        "C": 2,         # Official in South Korea and North Korea (using South Korea’s data)
        "G": 1947133,   # South Korea’s GDP
        # South Korea’s 2019 arrivals from Asia-Pacific table (~17.5 million)
        "T": 17.5,      
        "I": 54.6
    },
    "Iranian Persian": {
        "N": 78,
        "P": 60,        # Iran’s passport score is moderate-to-low
        "C": 3,         # Official in Iran, Afghanistan, and Tajikistan (approx.)
        "G": 1000000,   # an approximate combined GDP value
        # Iran’s 2019 arrivals from West Asia table (~9.1 million)
        "T": 9.1,       
        "I": 50
    },
    "Javanese": {
        "N": 68,
        "P": 80,        # similar to Indonesian
        "C": 1,
        "G": 1492618,   # Indonesia’s GDP (using the same value)
        # Using Indonesia’s 2019 arrivals (same as for Indonesian) (~15.5 million)
        "T": 15.5,      
        "I": 52
    },
    "Italian": {
        "N": 67,
        "P": 192,       # Italy’s passport is very strong
        "C": 4,         # Official in 4 countries
        "G": 2459597,   # Italy’s GDP
        # Italy’s 2023 arrivals from the top–10 international tourism destinations list (~57.2 million)
        "T": 57.2,      
        "I": 71.78
    },
    "Gujarati": {
        "N": 63,
        "P": 60,
        "C": 1,
        "G": 4271922,   # as an official language only in India
        # Using India’s 2019 arrivals (~17.9 million)
        "T": 17.9,      
        "I": 64.14
    },
    "Thai": {
        "N": 61,
        "P": 75,        # Thailand’s passport is modest
        "C": 1,
        "G": 545341,    # Thailand’s GDP (in millions)
        # Thailand’s 2019 arrivals from Asia-Pacific table (~39.8 million)
        "T": 39.8,      
        "I": 54.87
    },
    "Amharic": {
        "N": 60,
        "P": 40,        # Ethiopia’s passport (assumed low)
        "C": 1,
        "G": 300000,    # approximate GDP for Ethiopia
        "T": 0,        # No top–10 tourist arrival data available
        "I": 50
    },
    "Kannada": {
        "N": 59,
        "P": 60,
        "C": 1,
        "G": 4271922,   # using India’s GDP as proxy
        # Using India’s 2019 arrivals (~17.9 million)
        "T": 17.9,      
        "I": 64.14
    },
    "Levantine Arabic": {
        "N": 54,
        "P": 50,        # for example, using Lebanon’s passport (assumed)
        "C": 1,
        "G": 300000,    # approximate GDP for a small country like Lebanon
        # Lebanon’s 2019 arrivals from West Asia table (~1.9 million)
        "T": 1.9,       
        "I": 50
    },
    "Bhojpuri": {
        "N": 53,
        "P": 60,
        "C": 1,
        "G": 4271922,   # India’s GDP (as a proxy)
        # Using India’s 2019 arrivals (~17.9 million)
        "T": 17.9,      
        "I": 64.14
    },
}


# 2. Weights for Each Metric (summing to 1)
weights = {
    "N": 0.25,  # Number of speakers (e.g., in millions)
    "I": 0.20,  # Cultural influence index (from available rankings)
    "G": 0.175,  # Combined GDP (e.g., in trillion USD or millions US$)
    "C": 0.175,  # Number of countries where the language is official/de facto
    "T": 0.15,  # Number of tourist visitors (e.g., in millions of international arrivals)
    "P": 0.05,  # Passport strength index
}

# 3. List of Metrics
metrics = ["N", "I", "G", "C", "T", "P"]

# 4. Compute the minimum and maximum for each metric over all languages.
min_values = {}
max_values = {}
for metric in metrics:
    values = [languages_data[lang][metric] for lang in languages_data]
    min_values[metric] = min(values)
    max_values[metric] = max(values)

# Helper function: min–max normalization
def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0
    return (value - min_val) / (max_val - min_val)

# 5. Calculate normalized metrics and composite score for each language.
language_scores = {}
for language, data in languages_data.items():
    composite_score = 0
    normalized_metrics = {}
    for metric in metrics:
        norm_value = normalize(data[metric], min_values[metric], max_values[metric])
        normalized_metrics[metric] = norm_value
        composite_score += weights[metric] * norm_value
    language_scores[language] = {
        "normalized_metrics": normalized_metrics,
        "composite_score": composite_score
    }

# 6. Sort languages by composite score (highest first)
sorted_languages = sorted(language_scores.items(),
                          key=lambda item: item[1]["composite_score"],
                          reverse=True)

# 7. Output the results
print("Language Rankings based on Composite Usefulness Score:\n")
for rank, (language, info) in enumerate(sorted_languages, start=1):
    print(f"{rank}. {language}: Score = {info['composite_score']:.4f}")
    for metric in metrics:
        print(f"   Normalized {metric}: {info['normalized_metrics'][metric]:.4f}")
    print()
