subroutine get_default
    
    implicit none

    include "parameter.h"
    include "CB_variables.h"
    include "CB_const.h"

    double precision :: pi

!------------------------------------------------------------
! set parameter for the run
!------------------------------------------------------------

    k        =  1.5d7              ! normal stiffness
    ks       =  1.5d7              ! shear stiffness
    dt       =  5d-2               ! length of time step
    t        =  1000 * dt           ! length of time
    st       =  1                  ! divide tot num of timestep to st
    eta      =  1.5d1              ! Normal damping coefficient
    eta2     =  1.5d1              ! shear damping coefficient

    pi       =  4d0 * datan(1d0)   ! pi

    Cpair    =  1d03               ! Specific heat of air.
    Cpwater  =  4d03               ! Specific heat of water

    rhoair   =  1.3d0              ! air density [kg/m3]
    rhoice   =  9d02               ! ice density [kg/m3]
    rhowater =  1026d0             ! water density [kg/m3]

!------------------------------------------------------------
!           Disks physical parameters
!------------------------------------------------------------

    mass  =  rhoice * pi * h * r ** 2 

end subroutine get_default