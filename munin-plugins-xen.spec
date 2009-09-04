%define name	munin-plugins-xen
%define version	20080625
%define release	%mkrel 2

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

