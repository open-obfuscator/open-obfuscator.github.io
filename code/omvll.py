import omvll

def anti_hooking(self, _, func: omvll.Function):
    if func.demangled_name.startswith("hook_me"):
        return True
    return False

def obfuscate_struct_access(self, _, __, S: omvll.Struct):
    if S.name.endswith("JNINativeInterface"):
        return True
    return False

def obfuscate_string(self, _, func: omvll.Function, string):
    fname = func.demangled_name

    if b"/home/user/project/src/secret.cpp" in string:
        return "REDACTED"

    if fname == "Secret::encode(int)":
        return omvll.StringEncOptStack(20)

    if fname == "Secret::decode(int)":
        return True

    if fname == "Secret::help()":
        return omvll.StringEncOptGlobal()

    return False
