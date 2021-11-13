AC_INIT([onerng], [1], [paul@taniwha.com])
AM_INIT_AUTOMAKE()
m4_ifndef([PKG_PROG_PKG_CONFIG],
    [m4_fatal([Could not locate the pkg-config autoconf macros.
  These are usually located in /usr/share/aclocal/pkg.m4. If your macros
  are in a different location, try setting the environment variable
  ACLOCAL="aclocal -I /other/macro/dir" before running autoreconf.])])
PKG_PROG_PKG_CONFIG()
AC_PROG_CC
AC_ARG_WITH([udevrulesdir],
	AS_HELP_STRING([--with-udevrulesdir=DIR], [Directory for udev
rules]),
	[],
	[with_udevrulesdir=$($PKG_CONFIG --variable=udevdir udev)"/rules.d"])
AC_SUBST([udevrulesdir], [$with_udevrulesdir])

AC_CONFIG_FILES([
Makefile
files/Makefile
])
AC_OUTPUT

