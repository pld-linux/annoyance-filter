Summary:	Adaptive Bayesian Junk Mail Filter
Name:		annoyance-filter
Version:	1.0b
Release:	1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Applications/Mail
Source0:	http://www.fourmilab.ch/annoyance-filter/%{name}-%{version}.tar.gz
# Source0-md5:	f0910681eaa71bb71ab902d321e61e25
URL:		http://www.fourmilab.ch/annoyance-filter/
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
z
%description -l pl
z

%prep
%setup -q 


%build

export CFLAGS="%{rpmcflags} -fpermissive"
export CPPFLAGS="%{rpmcflags} -fpermissive"
%{__aclocal}
%{__autoconf}
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
