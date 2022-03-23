import senpy_club

print("SENPY_CLUB_API_BASE_URL:", senpy_club.SENPY_CLUB_API_BASE_URL)
print("SENPY_CLUB_API_CURRENT_VERSION:", senpy_club.SENPY_CLUB_API_CURRENT_VERSION)
print("SENPY_CLUB_API_URL:", senpy_club.SENPY_CLUB_API_URL)

random: senpy_club.Random = senpy_club.Random()
print("Random.image:", random.language)
print("Random.image:", random.image)

print("languages:", senpy_club.languages())
print("language(\"C\"):", senpy_club.language("C"))
