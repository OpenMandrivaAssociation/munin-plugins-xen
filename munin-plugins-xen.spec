%define name	munin-plugins-xen
%define version	20080625
%define release	4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Munin xen plugins
Group:		Networking/Other
License:	BSD
Source0:	http://www.skullkrusher.net/linux/scripts/xen_percent
Source1:    http://munin.projects.linpro.no/attachment/wiki/PluginCat/xen_traffic_all
Patch0:     xen_traffic_all-allow-multiple-interfaces.patch
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Munin plugins for monitoring xen.

%prep
%setup -c -T
cp %{SOURCE0} xen_percent
cp %{SOURCE1} xen_traffic_all
%patch0 -p 0

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/munin/plugins
install -m 755 xen_percent %{buildroot}%{_datadir}/munin/plugins
install -m 755 xen_traffic_all %{buildroot}%{_datadir}/munin/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/munin/plugin-conf.d
cat > %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/xen << EOF
[xen_traffic_all]
user root

[xen_percent]
user root

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/munin/plugins/*
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/xen



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20080625-3mdv2011.0
+ Revision: 620422
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20080625-2mdv2010.0
+ Revision: 430125
- rebuild

* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080625-1mdv2009.0
+ Revision: 229025
- import munin-plugins-xen


* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080625-1mdv2009.0
- first mandriva package
