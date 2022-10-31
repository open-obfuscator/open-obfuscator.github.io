# Mixed boolean-arithmetic Obfuscation
-obfuscate-arithmetic,high class re.dprotect.salsa20 {
  *;
}

# Strings protection
-obfuscate-strings "XEYnuNOGoEQ*", "TOKEN: *"
-obfuscate-strings class re.dprotect.Connect {
  private static java.lang.String API_KEY;
  public static java.lang.String getToken();
}

# Constants
-obfuscate-constants    class re.dprotect.secret.** { *; }

# Control-Flow
-obfuscate-control-flow class re.dprotect.internal.** { *; }
