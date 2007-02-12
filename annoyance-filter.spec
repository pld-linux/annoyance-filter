Summary:	Adaptive Bayesian junk mail filter
Summary(pl.UTF-8):	Adaptacyjny bayesowski filtr niechcianej poczty
Name:		annoyance-filter
Version:	1.0d
Release:	1
License:	Public Domain
Group:		Applications/Mail
Source0:	http://www.fourmilab.ch/annoyance-filter/%{name}-%{version}.tar.gz
# Source0-md5:	bb45c6264f9483888cc2fa50f897ac71
URL:		http://www.fourmilab.ch/annoyance-filter/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adaptive Bayesian junk mail filter.

%description -l pl.UTF-8
Adaptacyjny bayesowski filtr niechcianej poczty.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -fpermissive"
CPPFLAGS="%{rpmcflags} -fpermissive"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
