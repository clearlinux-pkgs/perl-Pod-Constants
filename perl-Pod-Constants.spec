#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Constants
Version  : 0.19
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/M/MG/MGV/Pod-Constants-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MG/MGV/Pod-Constants-0.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-constants-perl/libpod-constants-perl_0.19-1.debian.tar.xz
Summary  : 'Include constants from POD'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Pod-Constants-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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

%description dev
dev components for the perl-Pod-Constants package.


%package license
Summary: license components for the perl-Pod-Constants package.
Group: Default

%description license
license components for the perl-Pod-Constants package.


%prep
%setup -q -n Pod-Constants-0.19
cd ..
%setup -q -T -D -n Pod-Constants-0.19 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Pod-Constants-0.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-Constants
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Pod-Constants/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Pod-Constants/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/Pod/Constants.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Constants.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-Constants/LICENSE
/usr/share/package-licenses/perl-Pod-Constants/deblicense_copyright
