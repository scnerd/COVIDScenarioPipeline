def create_file_name(run_id,prefix,index,type,extension):
    return("%s%09d.%s.%s.%s" % (prefix,index,run_id,type,extension))

def create_file_name_without_extension(run_id,prefix,index,type):
    return("%s%09d.%s.%s" % (prefix,index,run_id,type))