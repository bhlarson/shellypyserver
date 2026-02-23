import os
import json
import yaml
import pickle

# To use S3: 
# from s3fs import S3FileSystem
# s3_creds = ReadDict(args.creds)['s3'][args.s3]
# fs = S3FileSystem(endpoint_url = s3_creds['address'], 
#                           key=s3_creds['access_key'],
#                           secret=s3_creds['secret_key'],
#                           use_ssl=s3_creds['tls'],)


def WriteDictJson(outdict, path, fs=None):

    jsonStr = json.dumps(outdict, indent=2, sort_keys=False)
    if fs is not None:
        # If using a filesystem like S3, write to the file system
        with fs.open(path, "w") as f:
            f.write(jsonStr)
    else:
        with open(path,"w") as f:
            f.write(jsonStr)
    return True

def ReadDictJson(filepath, fs=None):
    jsondict = None
    try:
        if fs is not None:
            # If using a filesystem like S3, read from the file system
            with fs.open(filepath) as json_file:
                jsondict = json.load(json_file)
        else:
            with open(filepath) as json_file:
                jsondict = json.load(json_file)
        if not jsondict:
            print('Failed to load {}'.format(filepath))
    except Exception as err:
        print("Exception {}: ReadDictJson failed to load {}.  {}".format(type(err), filepath, err))
        raise err
    return jsondict

def Dict2Json(outdict):
    jsonStr = json.dumps(outdict, sort_keys=False, indent=4)      
    return jsonStr

def Json2Dict(json_file):
    jsondict = json.load(json_file)
    return jsondict

def ReadDictYaml(filepath, fs=None):
    yamldict = {}
    try:
        if fs is not None:
            # If using a filesystem like S3, read from the file system
            with fs.open(filepath) as yaml_file:
                yamldict = yaml.safe_load(yaml_file)
        else:
            # Read from the local file system
            with open(filepath) as yaml_file:
                yamldict = yaml.safe_load(yaml_file)
        if not yamldict:
            print('Failed to load {}'.format(filepath))
    except Exception as err:
        print("Exception {}: ReadDictYaml failed to load {}.  {}".format(type(err), filepath, err))
        raise err
    return yamldict

def WriteDictYaml(outdict, path, fs=None):
    yamlStr = yaml.dump(outdict, indent=2, sort_keys=False)
    if fs is not None:
        # If using a filesystem like S3, write to the file system
        with fs.open(path, "w") as f:
            f.write(yamlStr)
    else:
        # Write to the local file system
        with open(path,"w") as f:
            f.write(yamlStr)
    return True

def ReadDictPickle(filepath, fs=None):
    pickledict = None
    if fs is not None:
        # If using a filesystem like S3, read from the file system
        with fs.open(filepath, 'rb') as pickle_file_obj:
            pickledict = pickle.load(pickle_file_obj)
    else:
        with open(filepath, 'rb') as pickle_file_obj:
            pickledict = pickle.load(pickle_file_obj)
    return pickledict

def WriteDictPickle(outdict, path, fs=None):
    if fs is not None:
        # If using a filesystem like S3, write to the file system
        with fs.open(path, 'wb') as pickle_file_obj:
            pickle.dump(outdict, pickle_file_obj)
    else:
        # Write to the local file system
        with open(path, 'wb') as pickle_file_obj:
            pickle.dump(outdict, pickle_file_obj)
    return True

def ReadDict(filepath, fs=None):
    if filepath[0] == '~':
        filepath = os.path.expanduser(filepath)
    ext = os.path.splitext(filepath)[1]
    if ext=='.yaml' or ext=='.yml':
        readDict = ReadDictYaml(filepath, fs)
    elif ext=='.pkl' or ext=='.pickle':
        readDict = ReadDictPickle(filepath, fs)
    elif ext=='.json':
        readDict = ReadDictJson(filepath, fs)
    else:
        readDict = None
    return readDict

def WriteDict(outdict, filepath, fs=None):
    if filepath[0] == '~':
        filepath = os.path.expanduser(filepath)
    ext = os.path.splitext(filepath)[1]
    if ext=='.yaml' or ext=='.yml':
        readDict = WriteDictYaml(outdict, filepath, fs)
    elif ext=='.pkl' or ext=='.pickle':
        readDict = WriteDictPickle(outdict, filepath, fs)
    elif ext=='.json':
        readDict = WriteDictJson(outdict, filepath, fs)
    else:
        readDict = None
    return readDict