Name: hunspell-hu
Summary: Hungarian hunspell dictionaries
Version: 1.5
Release: 3%{?dist}
Source: http://downloads.sourceforge.net/magyarispell/hu_HU-%{version}.tar.gz
Group: Applications/Text
URL: http://magyarispell.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Hungarian hunspell dictionaries.

%prep
%setup -q -n hu_HU-%{version}

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hu_HU.txt LEIRAS.txt
%{_datadir}/myspell/*

%changelog
* Fri Jan 08 2010 Caolan McNamara <caolanm@redhat.com> - 1.5-3
- Resolves: rhbz#553251 sync source with upstream

* Thu Jan 07 2010 Caolan McNamara <caolanm@redhat.com> - 1.5-2
- Resolves: rhbz#553251 sync source with upstream

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.5-1.1
- Rebuilt for RHEL 6

* Thu Sep 17 2009 Caolan McNamara <caolanm@redhat.com> - 1.5-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 1.4-1
- latest version

* Mon Mar 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.3-1
- latest version

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version

* Tue Oct 02 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 1.2-2
- clarify that this is tri-licenced

* Fri Jun 01 2007 Caolan McNamara <caolanm@redhat.com> - 1.2-1
- next version

* Sat May 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.1-1
- latest canonical version

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061105-2
- match licence

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20061105-1
- initial version
