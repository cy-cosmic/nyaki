from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"admin", "adminapp.urls", name="admin"),
    host(r".*", "nyakiapp.urls", name="main"),
)