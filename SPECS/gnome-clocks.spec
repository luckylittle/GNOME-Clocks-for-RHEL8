Name:           gnome-clocks
Version:        3.28.0
Release:        1%{?dist}
Summary:        Clock application designed for GNOME 3
License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Clocks
Source0:        gnome-clocks-3.28.0.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Clock application designed for GNOME 3

%global debug_package %{nil}
%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/usr/
cp -arv $RPM_BUILD_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/usr/* $RPM_BUILD_ROOT/usr/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc
%license
/usr/bin/*
/usr/share/*

%changelog
* Wed May 23 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Resolves: #1567476

* Thu Feb 23 2017 Matthias Clasen <mclasen@redhat.com> - 3.22.1-1
- Rebase to 3.22.1
  Resolves: #1386881

* Fri Jul  1 2016 Matthias Clasen <mclasen@redhat.com> - 3.14.1-2
- Update translations
  Resolves: #1272479

* Mon Mar 23 2015 Richard Hughes <rhughes@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Resolves: #1174592

* Fri Feb 28 2014 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-8
- Rebuild to build with -fstack-protector-strong (related: #1070808).

* Wed Feb 26 2014 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-7
- Add missing resource files (related: #1028079).
- Don't ignore removal of src/resources.c (related: #1028079).

* Tue Feb 18 2014 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-6
- Force regeneration of resources.c (related: #1028079).

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.2-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.2-4
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-3
- Complete translations (related: #1044472).

* Thu Dec 12 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-2
- Remove 'New' from global menu (related: 1028079).

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.0-1
- Update to 3.7.92

* Mon Mar 18 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.92-1
- New upstream release - 3.7.92

* Wed Mar  6 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.91-1
- New upstream release - 3.7.91

* Wed Feb 20 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.90-1
- New upstream release - 3.7.90. Moving to vala.

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-3
- Use python3-canberra

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-2
- pycairo is python3-cairo in python3 land.

* Wed Feb  6 2013 Yanko Kaneti <yaneti@declera.com> - 0.1.6-1
- Update to 0.1.6. Handle the move to autotools.

* Tue Dec  4 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.5-1
- Update to 0.1.5.
- Additionaly require gnome-desktop3 and libnotify

* Tue Oct 16 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.4-1
- Update to 0.1.4

* Mon Oct  1 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.3-2
- Add packaging snippets to update the icon cache

* Thu Sep 27 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.3-1
- Update to 0.1.3

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-3
- Actually update the License tag

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-2
- Use packaged pycanberra

* Wed Sep 26 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.2-1
- Latest from upstream - 0.1.2

* Sat Sep 15 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.1-2
- Address review issues. Separate bundled pycanberra licensing

* Thu Sep 13 2012 Yanko Kaneti <yaneti@declera.com> - 0.1.1-1
- Package for review
