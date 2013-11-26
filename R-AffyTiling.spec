%define		packname	AffyTiling

Summary:	Easy extraction of individual probes in Affymetrix tiling arrays
Name:		R-%{packname}
Version:	1.20.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	5cbc7db056fbd052bb5487123ed99efb
URL:		http://bioconductor.org/packages/release/bioc/html/affy.html
BuildRequires:	R
BuildRequires:	R-affxparser
BuildRequires:	R-affy
BuildRequires:	R-preprocessCore
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-affxparser
Requires:	R-affy
Requires:	R-preprocessCore
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides easy, fast functions for the extraction and
annotation of individual probes from Affymetrix tiling arrays.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs
