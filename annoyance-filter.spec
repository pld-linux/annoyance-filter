Summary:	Adaptive Bayesian junk mail filter
Summary(pl):	Adaptacyjny bayesowski filtr niechcianej poczty
Name:		annoyance-filter
Version:	1.0b
Release:	1
License:	Public Domain
Group:		Applications/Mail
Source0:	http://www.fourmilab.ch/annoyance-filter/%{name}-%{version}.tar.gz
# Source0-md5:	f0910681eaa71bb71ab902d321e61e25
URL:		http://www.fourmilab.ch/annoyance-filter/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adaptive Bayesian junk mail filter.

%description -l pl
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/*
