import folium

m = folium.Map([55.96916279, -3.167832662], zoom_start=4)

folium.Circle((55.96916279, -3.167832662), radius=804_672).add_to(m)
folium.Circle((55.96916279, -3.167832662), radius=1_609_344).add_to(m)

m.save("the_proclaimers.html")
