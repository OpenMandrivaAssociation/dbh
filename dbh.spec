%define	name  	dbh
%define version	4.5.0
%define	release	%mkrel 2

%define api_version	4.5
%define lib_major	4
%define lib_name	%mklibname %{name}- %{api_version} %{lib_major}

%define __libtoolize /bin/true

Summary:	Disk based hash library
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License:	LGPL
Group: 		System/Libraries
Source:		%{name}-%{version}.tar.bz2
URL:		http://dbh.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-root


%description 
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of 
electronic data, such as graphic information. With the multidimensional binary 
tree it is possible to mathematically prove that access time to any 
particular record is minimized (using the concept of critical points from 
calculus), which provides the means to construct optimized databases for 
particular applications.  

%package -n %{lib_name}
Summary:	Disk based hash library
Group:		System/Libraries

%description -n %{lib_name}
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of
electronic data, such as graphic information. With the multidimensional binary
tree it is possible to mathematically prove that access time to any
particular record is minimized (using the concept of critical points from
calculus), which provides the means to construct optimized databases for
particular applications.

%package -n %{lib_name}-devel
Summary:	Libraries and headerfiles for development with dbh
Group:		Development/Other
Provides:	dbh-devel = %{version}-%{release}
Provides:	dbh4-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}

%description -n %{lib_name}-devel
Libraries and headerfiles for development with dbh.


%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 


%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog examples/*.c examples/Makefile* doc/*.html
%{_libdir}/libdbh-*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/dbh.pc
%{_libdir}/libdbh.*a
%{_libdir}/libdbh.so


