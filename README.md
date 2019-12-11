# diploma2019
Smart lock based on face recognition

TODO:
1) Small updates
-Add security(password/login check) for administration page
-Move users_list, device_list and images_list from global variables into DB
-Remove hardcoded pathes
-Test system on Raspberry Pi(write different code than for Windows PC+arduino)
-Update requirments file
-Fill information pages on administration page
-Improve algorithm of searching face
-Use 1 libary for face reco(remove from live_video_streaming)

2) Program architecture change
-Add two-level authentication(mobile code, app aprove etc)
-Move server from device to remote
-Add email registration/confirmation
