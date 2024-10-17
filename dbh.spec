%define apiver 4.5
%define major 4
%define libname %mklibname %{name}- %{apiver} %{major}
%define develname %mklibname %{name} -d

Summary:	Disk based hash library
Name:		dbh
Version:	4.5.0
Release:	%mkrel 5
License:	LGPLv2+
Group:		System/Libraries
URL:		https://dbh.sourceforge.net/
Source:		http://downloads.sourceforge.net/dbh/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description 
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of 
electronic data, such as graphic information. With the multidimensional binary 
tree it is possible to mathematically prove that access time to any 
particular record is minimized (using the concept of critical points from 
calculus), which provides the means to construct optimized databases for 
particular applications.  

%package -n %{libname}
Summary:	Disk based hash library
Group:		System/Libraries

%description -n %{libname}
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of
electronic data, such as graphic information. With the multidimensional binary
tree it is possible to mathematically prove that access time to any
particular record is minimized (using the concept of critical points from
calculus), which provides the means to construct optimized databases for
particular applications.

%package -n %{develname}
Summary:	Libraries and headerfiles for development with dbh
Group:		Development/Other
Provides:	dbh-devel = %{version}-%{release}
Provides:	libdbh-devel = %{version}-%{release}
Provides:	dbh4-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Libraries and headerfiles for development with dbh.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libdbh-%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog examples/*.c examples/Makefile* doc/*.html
%{_includedir}/*
%{_libdir}/pkgconfig/dbh.pc
%{_libdir}/libdbh.*a
%{_libdir}/libdbh.so
