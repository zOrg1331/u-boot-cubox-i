Name: u-boot-cubox-i
Version: 2018.05
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: armh

# the same U-Boot for both boards
Provides: u-boot-hummingboard

Source: %name-%version-%release.tar

BuildRequires: dtc >= 1.4
BuildRequires: bc

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports Cubox-i and Hummingboard SolidRun boards.

%prep
%setup

%build
%make_build mx6cuboxi_defconfig all

%install
install -pm0644 -D SPL %buildroot%_datadir/u-boot/cubox-i/u-boot-spl.bin
install -pm0644 -D u-boot.img %buildroot%_datadir/u-boot/cubox-i/u-boot.bin

%files
%doc board/solidrun/mx6cuboxi/README
%_datadir/u-boot/*

%changelog
* Sat Jul 07 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2018.05-alt1
- initial
