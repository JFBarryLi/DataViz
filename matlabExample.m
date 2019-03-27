function matlabExample
  % Number of interior points in each direction
  nx = 180;
  ny = 180;

  % Geometry
  x_max =  0.05;
  x_min = -0.05;
  y_max =  0.05;
  y_min = -0.05;

  deltax = (x_max-x_min)/(nx+1);
  deltay = (y_max-y_min)/(ny+1);

  X = zeros(nx,ny);
  Y = zeros(nx,ny);
  Z = zeros(nx,ny);

  for i = 1:nx
    for j = 1:ny
        X(i,j) = x_min + i*deltax;
        Y(i,j) = y_min + j*deltay;
    end
  end

  % Temperature of boundary
  Tb = 20; % degrees Celsius

  % Thermal conductivity
  k = 0.25;


  % Build A matrix, T, BC, and S
  num = nx*ny;
  % Allocate space
  A = spalloc(num,num,5*num);
  T = zeros(num,1);
  S = zeros(num,1);
  BC = zeros(num,1);

  for j = 1:ny
    for i = 1:nx

      % Compute global index
      index = i + nx*(j-1);

      % Diagonal term
      A(index,index) = k*(2/deltax^2+2/deltay^2);

      % "x-direction" terms
      if i == 1
        BC(index) =  BC(index) + k* Tb / deltax^2;
      else
        A(index,index-1) = -k/deltax^2;
      end

      if i == nx
        BC(index) = BC(index) + k* Tb / deltax^2;
      else
        A(index,index+1) = -k/deltax^2;
      end

      % "y-direction" terms
      if j == 1
        BC(index) = BC(index) + k *Tb/deltay^2;
      else
        A(index,index-nx) = -k/deltay^2;
      end

      if j == ny
        BC(index) = BC(index) + k *Tb/deltay^2;
      else
        A(index,index+nx) = -k/deltay^2;
      end


      % Find x and y coordinates and S
      x = X(i,j);
      y = Y(i,j);
      S(index) = source(x,y);

      end %for "i"

  end %fill A, BC, and F

  RHS = S+BC;

  disp('Solving Linear System');
  drawnow();
  T = A\RHS;

  disp(sprintf('nx = %d, ny = %d, Max T = %0.7f degrees Celsius',nx,ny,max(T)));
  drawnow();

  % Fill Z matrix with T for plotting
  for j = 1:ny
    for i = 1:nx
          Z(i,j) = T(i+(j-1)*nx);
      end
  end

  figure(1)
  contourf(X,Y,Z);
  colorbar;
  xlabel('x');
  ylabel('y');
  title('Temperature Distribution')

  figure(2)
  surf(X,Y,Z);
  shading interp;
  xlabel('x');
  ylabel('y');
  zlabel('T');
  title('Temperature Distribution')

end

%  Source
function output = source(x,y)

  if abs(x) < 0.01 && abs(y) < 0.01
     output = 125000.0;
  else
     output = 0.0;
  end %if

end

