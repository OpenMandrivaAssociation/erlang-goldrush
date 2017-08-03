%global realname goldrush
%global upstream DeadZen
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:       erlang-%{realname}
Version:    0.1.8
Release:    %mkrel 3
Group:      Development/Erlang

Summary:    Small, fast event processing and monitoring for Erlang/OTP applications
License:    MIT
URL:		https://github.com/%{upstream}/%{realname}
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar


%description
A small Erlang app that provides fast event stream processing.


%prep
%autosetup -n %{realname}-%{version}


%build
%{rebar_compile}
%{rebar_doc}


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin
install -p -m 644 ebin/%{realname}.app ebin/*.beam %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin


%files
%license LICENSE
%{_erllibdir}/%{realname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 0.1.8-3.mga6
+ Revision: 1010315
- imported package erlang-goldrush

