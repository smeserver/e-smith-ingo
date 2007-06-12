Summary: e-smith specific INGO configuration and templates.
%define name e-smith-ingo
Name: %{name}
%define version 1.1
%define release 6
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-ingo-1.1-1.backends_php.patch
Patch1: e-smith-ingo-1.1-2.createlinks.patch
Patch2: e-smith-ingo-1.1-3.menuarray.patch
Patch3: e-smith-ingo-1.1-4.ingo_horde_registry_php.patch 
Patch4: e-smith-ingo-1.1-5.ingo_1.1.2_template.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.1
Requires: ingo-h3 >= 1.1
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: php
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: smeserver-ingo-menuarray

%changelog
* Wed May 9 2007 Shad L. Lords <slords@mail.com> 1.1-6
- Move pear module requires to e-smith-horde

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sat Dec 09 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Mon Oct 22 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-5
- Patch to upgrade template files to match ingo 1.1.2.

* Thu Oct 5 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-4
- Added ingo specific horde/config/registry.php settings.  These were previously
  kept in the e-smith-horde rpm.

* Sat Sep 23 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-3
- Added an includes statement to 120Menu that will grab the information in 
  horde/conf.menu.apps.php.  This way each of the individual horde modules 
  don't have to repeatedly process the same template for the menu array 
  section in conf.php.
- Added the ability to enable or disable ingo menu icon from showing up on the main 
  webmail screen.  To initially enable - config set ingo service MenuArray disabled|enabled
  After the DB entry is created you can enable or disable this by 
  config setprop ingo MenuArray disabled|enabled

* Sat Sep 23 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-2
- Patch to createlinks that moves symlink create function from spec file
  to createlinks section.

* Thu Sep 14 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-1
- Patch to backend.php templates to reflect changes in ingo 1.1.1

* Wed Sep 13 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.1-0
- Rolled to new dev stream to reflect work done for ingo 1.1.1

* Wed Jun 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-02
- Fix use of deprecated APIs in httpd.conf template fragment. [SME: 708]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au>
- Bump release number (and fix spelling in changelog entry)

* Sun Sep 18 2005 chris burnat <cburnat@burnat.com>
- [0.5.1-01sme02]
- Addentum: this package and its dependancy have been included into the 
  build to fix issues described in [SF:1276898] "webmail filters 
  disabled".  Thanks to Greg Swallow.

* Fri Sep 16 2005 chris burnat <cburnat@burnat.com>
- [0.5.1-01sme01]
- rebuild & change Release tag 

* Wed Aug 31 2005 Greg Swallow <gregswallow@skynetonline.ca>
- [0.5.1-01]
- initial release

%description
This package adds necessary templates and configuration items
so that INGO will work properly.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
 
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
