%global tl_name diffcoeff
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.6
Release:	%{tl_revision}.1
Summary:	Write differential coefficients easily and consistently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diffcoeff
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diffcoeff.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diffcoeff.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the easy and consistent writing of ordinary, partial
and other derivatives of arbitrary (algebraic or numeric) order. For
mixed partial derivatives, the total order of differentiation is
calculated by the package. Optional arguments allow specification of
points of evaluation (ordinary derivatives), or variables held constant
(partial derivatives), and the placement of the differentiand (numerator
or appended). The package is built on xtemplate and the configurability
it enables, extending to differentials (including simple line elements)
and jacobians.

