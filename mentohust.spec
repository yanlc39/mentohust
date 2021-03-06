Name:           mentohust
Version:        1.0.0
Release:        1%{?dist}
Summary:        A Ruijie and Cernet supplicant
Summary(zh_CN.UTF-8): 锐捷和塞尔认证

Group:          Applications/Internet
License:        BSD
URL:            http://code.google.com/p/mentohust/
Source0:        http://mentohust.googlecode.com/files/mentohust-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glibc-devel libpcap-devel
Requires:       libpcap

%description
This package contains a Ruijie and Cernet supplicant from HustMoon Studio.

See %{_defaultdocdir}/%{name}-%{version}/README for more information.

%description -l zh_CN.UTF-8
mentohust是用来进行锐捷和塞尔认证的。因为官方没有Linux版本或者Linux版本很不好用
^_^

详见 %{_defaultdocdir}/%{name}-%{version}/README


%prep
%setup -q


%build
%configure --docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/mentohust
%config %{_sysconfdir}/mentohust.conf
%{_mandir}/man1/mentohust*
%doc %{_defaultdocdir}/%{name}-%{version}/*

%changelog
