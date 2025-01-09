import math
import matplotlib.pyplot as plt
import numpy as np
#from scipy.spatial import Delaunay
import Delaunay_Triangulation
import obstacle_reader
import csv

####################################### USER INPUT ########################################
# Define the hospital from which the drone will take-off:
start_hospital = 'BRI' #'BRI' for Bristol Royal Infirmary, or 'SH' for Southmead Hospital
alt = 100 #chosen flight altitude above terrain (m)  
###########################################################################################

############################ Rest of the code (DO NOT CHANGE) #############################

## Coordinates of BRI and SH helipads ##

BRI_lat = 51.4589706947779
BRI_lon = -2.59624421596527

SH_lat = 51.4937088
SH_lon = -2.5925803

# Define where the drone will start (i.e. take-off)
def start_choose(start):
    if start == 'BRI':
        start_point = np.array([BRI_lon,BRI_lat])
        start_tri = 18 #triangle in which the start point is - manually determined from Delaunay. (!DO NOT CHANGE!)
        
    
        goal_point = np.array([SH_lon,SH_lat])
        goal_tri = 92 #triangle in which the goal point is - manually determined from Delaunay. (!DO NOT CHANGE!)
    
    elif start == 'SH':
        start_point = np.array([SH_lon,SH_lat])
        start_tri = 92 #triangle in which the start point is - manually determined from Delaunay. (!DO NOT CHANGE!)
    
        goal_point = np.array([BRI_lon,BRI_lat])
        goal_tri = 18 #triangle in which the goal point is - manually determined from Delaunay. (!DO NOT CHANGE!)
        
    return start_point, start_tri, goal_point, goal_tri
    
start_point, start_tri, goal_point, goal_tri = start_choose(start_hospital)


## Find the distance and bearing between helipads using the haversine formula ##

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in meters
    earth_radius = 6371000  # Approximate value, can vary slightly depending on the Earth model

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    # Calculate the bearing (angle) from the first point to the second point
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    bearing = math.degrees(math.atan2(y, x))

    # Normalize the bearing to a compass bearing between 0 and 360 degrees
    if bearing < 0:
        bearing += 360

    return distance, bearing

distance, bearing = haversine(BRI_lat,BRI_lon,SH_lat,SH_lon)
print(f"Distance between the two helipads: {round(distance,1)} metres")
print(f"Bearing from Bristol Royal Infirmary to Southmead Hospital: {round(bearing,2)} degrees")


## Plot to illustrate ##
plt.figure('Obstacle Visualisation')
# Plot the two points
plt.scatter([BRI_lon, SH_lon], [BRI_lat, SH_lat], color='green', label='Helipads')
plt.gca().set_aspect('equal', adjustable='datalim')

# Draw a line to represent the distance between the points
#plt.plot([BRI_lon, SH_lon], [BRI_lat, SH_lat], linestyle='--', color='blue', label='Distance')

# Set labels and legend
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid()
# Don't show the plot yet (will show obstacles & workspace as well)


## Define the workspace & obstacles ##

# First, define the area over which to evaluate (as [lon,lat]])
lat_margin = 0.0065 #i.e. ~700m
lon_margin = 0.0125 #i.e. ~1100m
outer_points = np.array([[BRI_lon-lon_margin,BRI_lat-lat_margin],[BRI_lon-lon_margin,SH_lat+lat_margin]
                        ,[SH_lon+lon_margin,SH_lat+lat_margin],[SH_lon+lon_margin,BRI_lat-lat_margin]])
# Extract outer points in a .poly file to visualise in MissionPlanner
output_file = "outer_boundary.poly"

# Write the coordinates to the text file
with open(output_file, 'w') as file:
    for lon, lat in outer_points:
        file.write(f"{lat} {lon}\n")


# Then define the obstacles. A function is created to read the obstacles from .poly
# files defined in MissionPlanner, using data from https://dronesafetymap.com

obstacles = obstacle_coord = obstacle_reader.obstacle_read()


## Plot to show the obstacles
def plot_poly(points,fmt='b-',**kwargs):
    plt.plot(np.append(points[:,0],points[0,0]),np.append(points[:,1],points[0,1]),fmt,**kwargs)

plot_poly(outer_points, 'b-', label='Workspace')
legend_flag = 0
for ob in obstacles:
    legend_flag = legend_flag + 1
    if legend_flag == 1:
        plot_poly(ob,'r-',label='Obstacles')
    else:
        plot_poly(ob,'r-')
plt.legend()
plt.title('Obstacle Visualisation')
plt.xlim(-2.63, -2.561)
plt.ylim(51.45, 51.505)
#plt.show()

### Now ready for Delaunay Algorithm ###
all_points, tri, path_nodes = Delaunay_Triangulation.delaunay_path(outer_points,obstacles,start_point,start_tri,goal_point,goal_tri)

## Mission Planner Waypoints 
# Note: The waypoints yield sharp turns. This can be overcome by enabling 'spline waypoints' in the waypoint file

# Constants (DO NOT CHANGE)
NAV_WAYPOINT = 16
NAV_SPLINE_WAYPOINT = 82 
NAV_LAND = 21
TAKEOFF = 22
MAV_FRAME_GLOBAL_TERRAIN_ALT = 10
MAV_FRAME_GLOBAL = 0

# Waypoints
def waypoint_write(alt,filename):
    home_lat = path_nodes[0][0]
    home_lon = path_nodes[0][1]
    
    waypoints = [[0,1,MAV_FRAME_GLOBAL_TERRAIN_ALT,NAV_WAYPOINT,0,0,0,0,home_lat,home_lon,0,1]]
    
    
    wp_idx = 0
    for lat,lon in path_nodes:
        wp_idx = wp_idx + 1
        
        if wp_idx == 1:
            waypoints.append([wp_idx,0,MAV_FRAME_GLOBAL_TERRAIN_ALT,TAKEOFF,0,0,0,0,lat,lon,alt,1])
            
        elif wp_idx == len(path_nodes):
            waypoints.append([wp_idx,0,MAV_FRAME_GLOBAL_TERRAIN_ALT,NAV_LAND,0,0,0,0,lat,lon,0,1])
            
        else:
            waypoints.append([wp_idx,0,MAV_FRAME_GLOBAL_TERRAIN_ALT,NAV_SPLINE_WAYPOINT,0,0,0,0,lat,lon,alt,1])
    
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['QGC WPL 110'])
        writer.writerows(waypoints)
        
    return waypoints      

waypoints = waypoint_write(alt,'MissionPlanner_Waypoints.txt')

plt.show()
