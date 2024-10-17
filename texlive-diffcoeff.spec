Name:		texlive-diffcoeff
Version:	68838
Release:	1
Summary:	Write differential coefficients easily and consistently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diffcoeff
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diffcoeff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diffcoeff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
diffcoeff.sty allows the easy and consistent writing of
ordinary, partial and other derivatives of arbitrary (algebraic
or numeric) order. For mixed partial derivatives, the total
order of differentiation is calculated by the package. Optional
arguments allow specification of points of evaluation (ordinary
derivatives), or variables held constant (partial derivatives),
and the placement of the differentiand (numerator or appended).
The package is built on xtemplate, allowing systematic
fine-tuning of the display and generation and use of variant
forms (like derivatives built from D, \Delta or \delta). A
command for differentials ensures the dx used in e.g. integrals
is consistent with the form used in derivatives. The package
requires the LaTeX3 bundles l3kernel and l3packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/diffcoeff
%doc %{_texmfdistdir}/doc/latex/diffcoeff

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
