%global srcname pyrsistent
%global mod_name pyrsistent

Summary:        Persistent/Functional/Immutable data structures
Name:           python-%{srcname}
Version:        0.14.2
Release:        4%{?dist}
License:        MIT
Source0:        https://files.pythonhosted.org/packages/source/p/%{mod_name}/%{mod_name}-%{version}.tar.gz
URL:            http://github.com/tobgu/pyrsistent/

%description
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.


%package -n python2-%{srcname}
Summary: Persistent/Functional/Immutable data structures
%{?python_provide:%python_provide python2-%{pkg_name}}
BuildRequires: python2-devel
BuildRequires: python2-six

%description -n python2-%{srcname}
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

Python 2 version.

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Persistent/Functional/Immutable data structures
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{srcname}
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

Python 3 version.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
#% {__python2} setup.py test
#% {__python3} setup.py test

%files  -n python2-%{srcname}
%license LICENCE.mit
%doc README.rst
%{python2_sitearch}/%{srcname}
%{python2_sitearch}/_%{srcname}_version.py*
%{python2_sitearch}/p*.so
%{python2_sitearch}/%{srcname}-%{version}-py?.?.egg-info/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENCE.mit
%doc README.rst
%{python3_sitearch}/__pycache__/_%{srcname}_*.pyc
%{python3_sitearch}/_%{srcname}_version.py
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info/*
%{python3_sitearch}/pvectorc.cpython*.so


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-4
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-3
- add missing dist-tag

* Fri Apr 13 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-2
- disable tests for now

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.14.2-1
- new version 0.14.2

* Wed Sep 14 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-2
- Fix packaging errors, that would own /usr/lib64 or so.

* Tue Sep 13 2016 Devrim Gündüz <devrim@gunduz.org> 0.11.13-1
- Initial packaging for PostgreSQL YUM repository, to satisfy
  pgadmin4 dependency.
