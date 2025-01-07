import numpy as np

def obstacle_read():
    
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_prison.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
    
    # Convert the list to a NumPy array
    obstacles = [np.array(obstacle_coord)]


    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_university.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
    
    # Add to the obstacle array
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_cothamschool.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))

    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_cothamgardens.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_montpeillerparkandschools.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_redlandgreen.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_cityofbristolcollege.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_centralbrisandcastlepark.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_standrewsgarden.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_memorialstadium.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_bishopplayfield.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_stbonaventures.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_horfieldcommon.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_henleazeschools.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_badockswood.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    # Repeat  
    obstacle_coord = []
    # Open the file for reading
    with open('obstacle_files/obstacle_armyreserve.poly', 'r') as file:
        # Read each line in the file
        lines = file.readlines()  # Read all lines into a list
        for line in lines[1:-1]:
            # Split each line into latitude and longitude values
            lat, lon = map(float, line.split())
            obstacle_coord.append([lon,lat])
            
    obstacles.append(np.array(obstacle_coord))
    
    
    return obstacles