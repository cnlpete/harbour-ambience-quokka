Name:       harbour-ambience-quokka

Summary:    My Quokka Ambiance
Version:    0.2.0
Release:    0.2
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
Vendor: Hauke Schade
Packager: Hauke Schade <cnlpete@cnlpete.de>

# This requirement is verboten for Harbour submission
Requires:   ambienced

%description
This is my quokka ambiance. It's a neat little kangaroo living near Perth, Australia.

%package ts-devel
Summary:   Translation source for %name
License:   TBD
Group:     System/GUI/Other

%description ts-devel
Translation source for %name

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
# Without the root directory specified it will not be removed on uninstall
%{_datadir}/ambience/%{name}
%{_datadir}/ambience/%{name}/%{name}.ambience
%{_datadir}/ambience/%{name}/sounds.index
%{_datadir}/ambience/%{name}/images/*
# %{_datadir}/ambience/%{name}/sounds/* # no sounds yet
%{_datadir}/translations/%{name}_eng_en.qm

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/%{name}.ts


# Scripts are verboten for Harbour submission, this is only needed for
# install methods _other_ than the Store.
%post
systemctl-user restart ambienced.service

