%define	major 0
%define libname	%mklibname srtp %{major}
%define develname %mklibname -d srtp

Summary:	Secure Real-time Transport Protocol (SRTP)
Name:		srtp
Version:	1.4.4
Release:	%mkrel 3
License:	GPL
Group:		System/Libraries
URL:		https://srtp.sourceforge.net/
Source0:	http://srtp.sourceforge.net/%{name}-%{version}.tgz
Patch0:		srtp-shared.diff
BuildRequires:	autoconf automake libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified
in RFC 3711.

%package -n	%{libname}
Summary:	Secure Real-time Transport Protocol (SRTP) library
Group:          System/Libraries

%description -n	%{libname}
SRTP is a security profile for RTP that adds confidentiality, message 
authentication, and replay protection to that protocol. It is specified 
in RFC 3711.

%package -n	%{develname}
Summary:	Development files for the SRTP library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	srtp-devel = %{version}-%{release}

%description -n	%{develname}
SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified 
in RFC 3711.

This package contains the development files for the Secure Real-time Transport
Protocol (SRTP) library

%prep

%setup -q -n %{name}
%patch0 -p1

# lib64 fix
#find -name "Makefile" | xargs perl -pi -e 's|\$\(INSTALL_BASE\)/lib|\$\(INSTALL_BASE\)/%{_lib}|g'

%build
autoreconf -fi

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"

%configure \
	--enable-pic \
	--enable-syslog \
	--enable-generic-aesicm

%make

%install
rm -rf %{buildroot}

%makeinstall

rm -f %{buildroot}%{_libdir}/*.*a

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc CHANGES README
%{_includedir}/%{name}/*
%{_libdir}/*.so
