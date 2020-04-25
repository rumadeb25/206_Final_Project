import matplotlib 
import matplotlib.pyplot as plt

with open('compare_census.txt') as f:
    lines = f.readlines()
    income = [line.split(',')[0] for line in lines[1:-1]]
    coverage = [line.split(',')[1] for line in lines[1:-1]]
    coverage = list(map(str.strip, coverage))
    #import pdb; pdb.set_trace()
    
plt.figure()
plt.scatter(income, coverage)
plt.xlabel("Median Income")
plt.ylabel("Num People with Insurance Coverage")
plt.show()






# base_url = s

# def setUpDatabase( ):
#     path = os.path.dirname(os.path.abspath(__file__))
#     conn = sqlite3.connect(path+'/'+ 'census.db')
#     cur = conn.cursor()
#     return cur, conn

# def readDataFromFile(filename):
#     full_path = os.path.join(os.path.dirname(__file__), filename)
#     f = open(full_path)
#     file_data = f.read()
#     f.close()
#     json_data = json.loads(file_data)
#     return json_data


# def read_cache(CACHE_FNAME):
#     """
#     This function reads from the JSON cache file and returns a dictionary from the cache data.
#     If the file doesn't exist, it returns an empty dictionary.
#     """
#     try:
#         cache_file = open(CACHE_FNAME, 'r', encoding="utf-8") # Try to read the data from the file
#         cache_contents = cache_file.read()  # If it's there, get it into a string
#         CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
#         cache_file.close() # Close the file, we're good, we got the data in a dictionary.
#         return CACHE_DICTION
#     except:
#         CACHE_DICTION = {}
#         return CACHE_DICTION

# def write_cache(CACHE_FNAME, CACHE_DICT):
#     json_format  = json.dumps(CACHE_DICT)
#     f = open(CACHE_FNAME, "w")
#     f.write(json_format)
#     f.close()



# fh = open("  .data")

# def create_request_url( ):

# getting data from the web 
# creating an api request with the request url 

    # parms = 
    # request_url =  base_url + parms
    # r = requests.get(request_url)
    

    # try:
    #     dict = json.loads(r.text)
    # except:
    #     print("error when reading from url")  
    #     dict = {}



