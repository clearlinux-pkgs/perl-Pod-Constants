#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Pod-Constants
Version  : 0.19
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/M/MG/MGV/Pod-Constants-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MG/MGV/Pod-Constants-0.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-constants-perl/libpod-constants-perl_0.19-1.debian.tar.xz
Summary  : 'Include constants from POD'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Pod-Constants-license = %{version}-%{release}
Requires: perl-Pod-Constants-perl = %{version}-%{release}
Requires: perl(Pod::Parser)
BuildRequires : buildreq-cpan
BuildRequires : perl(Pod::Parser)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Pod::Constants version 0.19
===========================
Pod::Constants allows you to extract data from your POD at run-time,
meaning you can do things like declare constants in POD and not have
to update two places at once every time you make a change.

%package dev
Summary: dev components for the perl-Pod-Constants package.
Group: Development
Provides: perl-Pod-Constants-devel = %{version}-%{release}
Requires: perl-Pod-Constants = %{version}-%{release}

%description dev
dev components for the perl-Pod-Constants package.


%package license
Summary: license components for the perl-Pod-Constants package.
Group: Default

%description license
license components for the perl-Pod-Constants package.


%package perl
Summary: perl components for the perl-Pod-Constants package.
Group: Default
Requires: perl-Pod-Constants = %{version}-%{release}

%description perl
perl components for the perl-Pod-Constants package.


%prep
%setup -q -n Pod-Constants-0.19
cd %{_builddir}
tar xf %{_sourcedir}/libpod-constants-perl_0.19-1.debian.tar.xz
cd %{_builddir}/Pod-Constants-0.19
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Pod-Constants-0.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-Constants
cp %{_builddir}/Pod-Constants-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Pod-Constants/3dba87fdd2fcb5c3cc93f325c7d938f24e976af1 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Pod-Constants/8dcb8863bef54e5bdd8046c1a13a6dbebf94b7e9 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Constants.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-Constants/3dba87fdd2fcb5c3cc93f325c7d938f24e976af1
/usr/share/package-licenses/perl-Pod-Constants/8dcb8863bef54e5bdd8046c1a13a6dbebf94b7e9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
